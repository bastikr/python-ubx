import struct

from .datatype import DataType
from .lists import List


class AtomicVariable(DataType):
    __slots__ = "name", "struct_format", "struct"

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

    def __mul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        return List(n*[self])

    def __rmul__(self, n):
        return self.__mul__(n)


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
