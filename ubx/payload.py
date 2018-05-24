import struct
from collections import OrderedDict

import bitarray


class PayloadError(Exception):
    def __init__(self, msg, buffer, context, suberror=None):
        if isinstance(suberror, Exception):
            submessage = "\n- " + str(suberror)
        elif isinstance(suberror, (tuple, list)):
            submessage = "\n- " + "\n- ".join(map(str, suberror))
        else:
            submessage = ""
        msg = msg + submessage.replace("\n", "\n  ")

        Exception.__init__(self, msg)
        self.msg = msg
        self.buffer = buffer
        self.context = context
        self.suberror = suberror


class Context:
    def __init__(self, data=None, parent=None):
        self.data = data
        self.parent = parent

    @staticmethod
    def child(context, data):
        return Context(data=data, parent=context)


class Buffer:
    def __init__(self, data, index):
        self.data = data
        self.index = index

    @property
    def remaining_bytesize(self):
        return len(self.data) - self.index

    def reset(self):
        self.index = 0

    def read(self, n):
        selection = self.data[self.index:self.index+n]
        self.index += n
        return selection

    def check_bytesize(self, bytesize, name, context):
        if bytesize is not None and self.remaining_bytesize < bytesize:
            raise PayloadError("Not enough remaining bytes ({}) to parse {} of size {}".format(
                    self.remaining_bytesize, name, bytesize),
                                self, context)

class EmptyVariable:
    bytesize = 0

    def parse(self, buffer, context=None):
        return None

    def serialize(self, content, context=None):
        if content is not None:
            raise PayloadError("Content to be serialized by EmptyVariable is not None.", content, context)
        return b""

    def __str__(self):
        return "Empty"


Empty = EmptyVariable()


class AtomicVariable:
    def __init__(self, name, bytesize, struct_format):
        self.name = name
        self.bytesize = bytesize
        self.struct_format = struct_format
        self.struct = struct.Struct("<" + self.struct_format)

    def parse(self, buffer, context=None):
        buffer.check_bytesize(self.bytesize, self.name, context)
        bytestring = buffer.read(self.bytesize)
        return self.struct.unpack(bytestring)[0]

    def serialize(self, content, context=None):
        return self.struct.pack(content)

    def __str__(self):
        return self.name


class BitfieldEntry:
    def __init__(self, name, bits):
        self.name = name
        self.bits = bits

    def parse(self, bitarray):
        return bitarray[self.bits]

    def serialize(self, content, bitarray, context=None):
        bitarray[self.bits] = content[self.name]

    def __str__(self):
        return "BitfieldEntry(name=\"{}\"; bits={})".format(self.name, self.bits)


class Bitfield:
    def __init__(self, bytesize, entries=None):
        self.bytesize = bytesize
        self.entries = entries

    def parse(self, buffer, context=None):
        buffer.check_bytesize(self.bytesize, "Bitfield", context)
        bytestring = buffer.read(self.bytesize)
        bits = bitarray.bitarray(endian="little")
        bits.frombytes(bytestring)
        if self.entries is None:
            return bits
        d = OrderedDict()
        for entry in self.entries:
            d[entry.name] = entry.parse(bits)
        return d

    def serialize(self, content, context=None):
        if isinstance(content, bitarray.bitarray):
            return content.tobytes()
        if not isinstance(content, (dict, OrderedDict)):
            raise PayloadError("Serialization error in Bitfield: content must be dict or OrderedDict but is {}.".format(
                type(content)), content, context)
        if self.entries is None:
            raise PayloadError("Serialization error in Bitfield: Description is None but content is {}.".format(
                type(content)), content, context)
        subcontext = Context.child(context, content)
        bits = bitarray.bitarray(8*self.bytesize, endian="little")
        bits.setall(False)
        for entry in self.entries:
            entry.serialize(content, bits, subcontext)
        return bits.tobytes()

    def __str__(self):
        header = "Bitfield({})".format(self.bytesize)
        if self.entries is None:
            return header
        return header + ":\n" + "\n".join(["  * "+str(entry) for entry in self.entries])


U1 = AtomicVariable("U1", 1, "B")
U2 = AtomicVariable("U2", 2, "H")
U4 = AtomicVariable("U4", 4, "L")
U8 = AtomicVariable("U8", 8, "Q")

I1 = AtomicVariable("I1", 1, "b")
I2 = AtomicVariable("I2", 2, "h")
I4 = AtomicVariable("I4", 4, "l")
I8 = AtomicVariable("I8", 8, "q")

R4 = AtomicVariable("R4", 4, "f")
R8 = AtomicVariable("R8", 8, "d")

X1 = Bitfield(1)
X2 = Bitfield(2)
X4 = Bitfield(4)
X8 = Bitfield(8)


class Chars:
    def __init__(self, bytesize):
        self.bytesize = bytesize

    def parse(self, buffer, context=None):
        buffer.check_bytesize(self.bytesize, "Chars", context)
        if self.bytesize is None:
            bytestring = buffer.read(buffer.remaining_bytesize)
        else:
            bytestring = buffer.read(self.bytesize)
        return bytestring.decode("iso-8859-1")

    def serialize(self, content, context=None):
        return content.encode("iso-8859-1")

    def __str__(self):
        return "Chars({})".format(self.bytesize)


class Fields(OrderedDict):
    def __init__(self, *fields):
        OrderedDict.__init__(self, fields)
        bytesize = 0
        for _, description in fields:
            if not hasattr(description, "bytesize") or description.bytesize is None:
                bytesize = None
                break
            else:
                bytesize += description.bytesize
        self.bytesize = bytesize

    def parse(self, buffer, context=None):
        buffer.check_bytesize(self.bytesize, "Fields", context)
        data = OrderedDict()
        subcontext = Context.child(context, data)
        for name, description in self.items():
            try:
                data[name] = description.parse(buffer, subcontext)
            except PayloadError as e:
                raise PayloadError("Fields: PayloadError while parsing the field {}.".format(name),
                                   buffer, context, e)
        return data

    def serialize(self, content, context=None):
        if not isinstance(content, (dict, OrderedDict)):
            raise PayloadError("Serialization error in Fields: content must be dict or OrderedDict but is {}.".format(
                type(content)), content, context)
        if len(content) != len(self):
            raise PayloadError("Serialization error in Fields: length of content is {} instead of {}.".format(
                len(content), len(self)), content, context)
        subcontext = Context.child(context, content)
        data = []
        for name, description in self.items():
            if name not in content:
                raise PayloadError("Serialization error in Fields: content has no field with name {}.".format(name),
                    content, context)
            try:
                data.append(description.serialize(content[name], subcontext))
            except PayloadError as e:
                raise PayloadError("Serialization error in field {}.".format(name),
                    content, context, e)
        return b"".join(data)

    def __str__(self):
        description_strings = []
        for name, description in self.items():
            description_string = str(description)
            if "\n" in description_string:
                description_string = description_string.replace("\n", "\n    ")
                description_strings.append("{}:\n    {}".format(name, description_string))
            else:
                description_strings.append("{}: {}".format(name, description_string))
        if self.bytesize is None:
            sizestring = "?"
        else:
            sizestring = str(self.bytesize)
        return "Fields(length=" + sizestring + ") {\n  " + ",\n  ".join(description_strings) + "\n}"


class List:
    def __init__(self, descriptions):
        self.descriptions = descriptions
        bytesize = 0
        for description in descriptions:
            if not hasattr(description, "bytesize") or description.bytesize is None:
                bytesize = None
                break
            else:
                bytesize += description.bytesize
        self.bytesize = bytesize

    def parse(self, buffer, context=None):
        buffer.check_bytesize(self.bytesize, "List", context)
        data = []
        subcontext = Context.child(context, data)
        for i, description in enumerate(self.descriptions):
            try:
                data.append(description.parse(buffer, subcontext))
            except PayloadError as e:
                raise PayloadError("List description: PayloadError while parsing entry number {}.".format(i),
                                   buffer, context, e)
        return data

    def serialize(self, content, context=None):
        if not isinstance(content, (list, tuple)):
            raise PayloadError("Serialization error in list: content must be list or tuple but is {}.".format(
                type(content)), content, context)
        if len(content) != len(self.descriptions):
            raise PayloadError("Serialization error in list: length of content is {} instead of {}.".format(
                len(content), len(self.descriptions)), content, context)
        subcontext = Context.child(context, content)
        data = []
        for i, description in enumerate(self.descriptions):
            try:
                data.append(description.serialize(content[i], subcontext))
            except PayloadError as e:
                raise PayloadError("Serialization error in list entry number {}".format(i),
                    content, context, e)
        return b"".join(data)

    def __str__(self):
        return "[\n  " +\
               ",\n  ".join([str(d).replace("\n", "\n  ")
                             for d in self.descriptions]) +\
               "\n]"


class Loop:
    def __init__(self, description):
        self.description = description
        self.bytesize = None

    def iterations(self, buffer, context):
        raise NotImplementedError()

    def parse(self, buffer, context):
        n = self.iterations(buffer, context)
        data = []
        subcontext = Context.child(context, data)
        for i in range(n):
            try:
                data.append(self.description.parse(buffer, subcontext))
            except PayloadError as e:
                raise PayloadError("Loop description: Payload error in iteration {}/{}.".format(i+1, n),
                                   buffer, context, e)
        return data

    def serialize(self, content, context=None):
        subcontext = Context.child(context, content)
        data = []
        if not isinstance(content, (list, tuple)):
            raise PayloadError("Serialization error in loop: content must be list or tuple but is {}.".format(
                type(content)), content, context)
        try:
            for i, entry in enumerate(content):
                data.append(self.description.serialize(entry, subcontext))
        except PayloadError as e:
            raise PayloadError("Serialization error in loop iteration {}".format(i),
                content, context, e)

        return b"".join(data)


class MatchedLoop(Loop):
    def __init__(self, description):
        if description.bytesize is None:
            raise ValueError("Description of matched loop has to have a fixed byte size.")
        Loop.__init__(self, description)

    def iterations(self, buffer, context):
        n, m = divmod(buffer.remaining_bytesize, self.description.bytesize)
        if m!=0:
            raise PayloadError("Matched loop of content length {} doesn't match input of length{}".format(
                self.description.bytesize, buffer.remaining_bytesize), buffer, context)
        return n

    def __str__(self):
        return "MatchedLoop:\n| " +\
               str(self.description).replace("\n", "\n| ")


class KeyLoop(Loop):
    def __init__(self, key, description):
        Loop.__init__(self, description)
        self.key = key

    def iterations(self, buffer, context):
        return context.data[self.key]

    def __str__(self):
        return "Loop(key=\"{}\"):\n| ".format(self.key) +\
               str(self.description).replace("\n", "\n| ")


class Options:
    def __init__(self, *descriptions):
        self.descriptions = descriptions

    def parse(self, buffer, context=None):
        payload_errors = []
        for description in self.descriptions:
            if description.bytesize is not None and buffer.remaining_bytesize != description.bytesize:
                payload_errors.append(PayloadError(
                    "Description bytesize ({}) doesn't match remaining bytesize ({})".format(
                        description.bytesize, buffer.remaining_bytesize),
                    buffer, context))
                continue
            try:
                return description.parse(buffer, context)
            except PayloadError as e:
                payload_errors.append(e)
                buffer.reset()
                continue
        raise PayloadError("All available description options failed.",
                           buffer, context, payload_errors)

    def serialize(self, content, context=None):
        payload_errors = []
        subcontext = Context.child(context, content)
        for description in self.descriptions:
            try:
                return description.serialize(content, subcontext)
            except PayloadError as e:
                payload_errors.append(e)
        raise PayloadError("All available description options failed.",
                           content, context, payload_errors)

    def __str__(self):
        options = []
        for i, d in enumerate(self.descriptions):
            options.append("  [{}]: ".format(i) + str(d).replace("\n", "\n    "))
        return "Options:\n" + "\n".join(options)
