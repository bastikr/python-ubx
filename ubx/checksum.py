"""
UBX Checksum.

Uses the 8-Bit Fletcher Algorithm.
"""

import struct


class Checksum:
    checksum_struct = struct.Struct("<B")

    def __init__(self, a=0, b=0):
        assert isinstance(a, int)
        assert isinstance(b, int)
        self.a = a
        self.b = b

    def update(self, byte):
        self.a = (self.a + ord(byte)) & 0xFF
        self.b = (self.b + self.a) & 0xFF

    def __repr__(self):
        return "Checksum({}, {})".format(self.a, self.b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not (self == other)

    def bytes(self):
        return self.checksum_struct.pack(self.a)\
             + self.checksum_struct.pack(self.b)


def calculate(*args):
    c = Checksum()
    for arg in args:
        for byte in arg:
            c.update(byte)
    return c
