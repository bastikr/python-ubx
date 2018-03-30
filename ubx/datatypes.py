import struct

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

X1 = Bitfield(1)
X2 = Bitfield(2)
X4 = Bitfield(4)
X8 = Bitfield(8)
