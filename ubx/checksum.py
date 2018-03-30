"""
UBX Checksum.

Uses the 8-Bit Fletcher Algorithm.
"""
class Checksum:
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

def calculate(*args):
    c = Checksum()
    for arg in args:
        for byte in arg:
            print(type(byte))
            c.update(byte)
    return c
