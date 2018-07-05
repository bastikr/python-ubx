"""Checksum using the 8-Bit Fletcher Algorithm with modulo 256."""

import sys
import struct


class ChecksumError(Exception):
    """Checksums don't match."""

    def __init__(self, checksum0, checksum1):
        Exception.__init__(self, "Checksums differ: {} vs {}".format(
            hex(checksum0.a) + hex(checksum0.a),
            hex(checksum1.a) + hex(checksum1.b)))
        self.checksum0 = checksum0
        self.checksum1 = checksum1


class Checksum:
    """Checksum using a 8-Bit Fletcher algorithm with modulo 256."""

    checksum_struct = struct.Struct("<B")

    def __init__(self, a=0, b=0):
        assert isinstance(a, int)
        assert isinstance(b, int)
        self.a = a
        self.b = b

    if sys.version_info > (3,):
        @staticmethod
        def from_bytestrings(*args):
            """Calculate a combined Checksum for the given bytestrings."""
            a = 0
            b = 0
            for arg in args:
                for x in arg:
                    a += x
                    b += a
            return Checksum(a & 0xFF, b & 0xFF)
    else:
        @staticmethod
        def from_bytestrings(*args):
            """Calculate a combined Checksum for the given bytestrings."""
            a = 0
            b = 0
            for arg in args:
                for byte in arg:
                    a += ord(byte)
                    b += a
            return Checksum(a & 0xFF, b & 0xFF)

    def update(self, byte):
        """Update the Checksum using te given single byte."""
        self.a = (self.a + ord(byte)) & 0xFF
        self.b = (self.b + self.a) & 0xFF

    def __repr__(self):
        return "Checksum({}, {})".format(self.a, self.b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not self == other

    def bytes(self):
        """Return a byte representation of this Checksum."""
        return self.checksum_struct.pack(self.a)\
             + self.checksum_struct.pack(self.b)

    def check_equal(self, other):
        """Raise a ChecksumError if the two Checksums are not equal."""
        if self != other:
            raise ChecksumError(self, other)
