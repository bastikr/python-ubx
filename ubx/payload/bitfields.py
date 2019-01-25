from collections import OrderedDict
import bitarray

from .datatype import DataType
from .lists import List
from .context import Context
from .exceptions import PayloadError


class BitfieldEntry(object):
    __slots__ = "name", "bits"

    def __init__(self, name, bits):
        self.name = name
        self.bits = bits

    def parse(self, bitarray):
        return bitarray[self.bits]

    def serialize(self, content, bitarray, context=None):
        bitarray[self.bits] = content[self.name]

    def __str__(self):
        return "BitfieldEntry(name=\"{}\"; bits={})".format(self.name, self.bits)


class Bitfield(DataType):
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

    def __mul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        return List(n*[self])

    def __rmul__(self, n):
        return self.__mul__(n)


X1 = Bitfield(1)
X2 = Bitfield(2)
X4 = Bitfield(4)
X8 = Bitfield(8)
