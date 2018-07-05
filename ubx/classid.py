"""UBX message classes."""

from . import utils


class ClassId:
    """
    Simple class storing the name and byte of a UBX message class.
    """
    def __init__(self, name, byte):
        self.name = name
        self.byte = byte

    def __eq__(self, other):
        if isinstance(other, ClassId):
            return self.name==other.name and self.byte==other.byte
        else:
            return NotImplemented

    def __ne__(self, other):
        return not self==other


ids = [
    ClassId("NAV", b"\x01"),
    ClassId("RXM", b"\x02"),
    ClassId("INF", b"\x04"),
    ClassId("ACK", b"\x05"),
    ClassId("CFG", b"\x06"),
    ClassId("UPD", b"\x09"),
    ClassId("MON", b"\x0a"),
    ClassId("AID", b"\x0b"),
    ClassId("TIM", b"\x0d"),
    ClassId("ESF", b"\x10"),
    ClassId("MGA", b"\x13"),
    ClassId("LOG", b"\x21"),
    ClassId("SEC", b"\x27"),
    ClassId("HNR", b"\x28"),
]
"""UBX message classes."""


# Insert message classes into module namespace
for id in ids:
    globals()[id.name] = id


def get_by_name(name):
    """Obtain the message class with the given name.

    Raises a ValueError if no message class matches the given name.
    """
    for id in ids:
        if id.name==name:
            return id
    raise ValueError("Unknown ClassId of name \"{}\".".format(name))


def get_by_byte(byte):
    """Obtain the message class with the given byte.

    Raises a ValueError if no message class matches the given byte.
    """
    if not isinstance(byte, bytes):
        raise TypeError("Expected byte argument to be of type \"bytes\" but it is \"{}\".".format(type(byte)))
    for id in ids:
        if id.byte==byte:
            return id
    raise ValueError("Unknown ClassId with byte \"0x{}\".".format(utils.byte2hexstring(byte)))
