import struct
from collections import OrderedDict

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
    
    def read(self, n):
        selection = self.data[self.index:self.index+n]
        self.index += n
        return selection


class AtomicVariable:
    def __init__(self, name, bytesize, struct_format):
        self.name = name
        self.bytesize = bytesize
        self.struct_format = struct_format
        self.struct = struct.Struct("<" + self.struct_format)

    def unpack(self, bytestring):
        if self.bytesize is not None and self.bytesize!=len(bytestring):
            raise ValueError("Given string doesn't match the expected size.")
        return self.struct.unpack(bytestring)[0]

    def parse(self, buffer, context=None):
        bytestring = buffer.read(self.bytesize)
        return self.unpack(bytestring)


class Bitfield(AtomicVariable):

    def __init__(self, bytesize):
        name = "X" + str(bytesize)
        struct_format = str(bytesize) + "s"
        AtomicVariable.__init__(self, name, bytesize, struct_format)


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


class Field:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Fields:
    def __init__(self, *fields):
        self.fields = fields

    def parse(self, buffer, context=None):
        data = OrderedDict()
        subcontext = Context.child(context, data)
        for field in self.fields:
            data[field.name] = field.parse(buffer, subcontext)
        return data


class List:
    def __init__(self, descriptions):
        self.descriptions = descriptions

    def parse(self, buffer, context=None):
        data = []
        subcontext = Context.child(context, data)
        for description in self.descriptions:
            data.append(description.parse(buffer, subcontext))
        return data


class Loop:
    def __init__(self, key, description):
        self.key = key
        self.description = description

    def parse(self, buffer, context):
        n = context.data[self.key]
        data = []
        subcontext = Context.child(context, data)
        for _ in range(n):
            data.append(self.description.parse(buffer, subcontext))
        return data

