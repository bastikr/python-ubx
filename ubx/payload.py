import struct
from collections import OrderedDict


class PayloadError(Exception):
    def __init__(self, msg, buffer, context, suberror=None):
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


class EmptyVariable:
    bytesize = 0

    def parse(self, buffer, context=None):
        return None

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
        if buffer.remaining_bytesize < self.bytesize:
            raise PayloadError("Not enough remaining bytes ({}) to parse {} of size {}".format(
                                    buffer.remaining_bytesize,
                                    self.name, self.bytesize),
                                buffer, context
                            )
        bytestring = buffer.read(self.bytesize)
        return self.struct.unpack(bytestring)[0]

    def __str__(self):
        return self.name


class Bitfield(AtomicVariable):

    def __init__(self, bytesize):
        name = "X" + str(bytesize)
        struct_format = str(bytesize) + "s"
        AtomicVariable.__init__(self, name, bytesize, struct_format)

    def __str__(self):
        return "Bitfield({})".format(self.bytesize)


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
        if self.bytesize is not None and buffer.remaining_bytesize < self.bytesize:
            raise PayloadError("Not enough remaining bytes ({}) to parse fields of size {}".format(
                                    buffer.remaining_bytesize,
                                    self.bytesize),
                                buffer, context
                            )
        data = OrderedDict()
        subcontext = Context.child(context, data)
        for name, description in self.items():
            try:
                data[name] = description.parse(buffer, subcontext)
            except PayloadError as e:
                raise PayloadError("Fields: PayloadError while parsing the field {}.".format(name),
                                    buffer, context, e)
        return data

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
        if self.bytesize is not None and buffer.remaining_bytesize < self.bytesize:
            raise PayloadError("Not enough remaining bytes ({}) to parse list of size {}".format(
                                    buffer.remaining_bytesize,
                                    self.bytesize),
                                buffer, context
                            )
        data = []
        subcontext = Context.child(context, data)
        for i, description in enumerate(self.descriptions):
            try:
                data.append(description.parse(buffer, subcontext))
            except PayloadError as e:
                raise PayloadError("List description: PayloadError while parsing entry number {}.".format(i),
                                    buffer, context, e)
        return data

    def __str__(self):
        return "[\n  " +\
               ",\n  ".join([str(d).replace("\n", "\n  ")
                            for d in self.descriptions]) +\
               "\n]"


class Loop:
    def __init__(self, key, description):
        self.key = key
        self.description = description
        self.bytesize = None

    def parse(self, buffer, context):
        n = context.data[self.key]
        data = []
        subcontext = Context.child(context, data)
        for i in range(n):
            try:
                data.append(self.description.parse(buffer, subcontext))
            except PayloadError as e:
                raise PayloadError("Loop description: Payload error in iteration {}.".format(i),
                                    buffer, context, e)
        return data

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
                continue
            try:
                return description.parse(buffer, context)
            except PayloadError as e:
                payload_errors.append(e)
                buffer.reset()
                continue
        raise PayloadError("All available description options failed.",
                            buffer, context, payload_errors)

    def __str__(self):
        options = ["  * " + str(d).replace("\n", "\n    ") for d in self.descriptions]
        return "Options:\n" + "\n".join(options)
