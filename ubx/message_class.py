"""UBX message classes."""

from . import utils


class MessageClass:
    """
    Simple class storing the name and byte of a UBX message class.
    """
    def __init__(self, name, byte):
        if not isinstance(byte, bytes):
            raise TypeError("byte argument has to be of type \"byte\" but is: {}".format(
                type(byte)))
        self.name = name
        self.byte = byte

    def __eq__(self, other):
        if isinstance(other, MessageClass):
            return self.name==other.name and self.byte==other.byte
        else:
            return NotImplemented

    def __ne__(self, other):
        return not self==other

    def __str__(self):
        bytestring = utils.byte2hexstring(self.byte)
        return "MessageClass(name={}, byte=0x{})".format(self.name, bytestring)


classes = [
    MessageClass("NAV", b"\x01"),
    MessageClass("RXM", b"\x02"),
    MessageClass("INF", b"\x04"),
    MessageClass("ACK", b"\x05"),
    MessageClass("CFG", b"\x06"),
    MessageClass("UPD", b"\x09"),
    MessageClass("MON", b"\x0a"),
    MessageClass("AID", b"\x0b"),
    MessageClass("TIM", b"\x0d"),
    MessageClass("ESF", b"\x10"),
    MessageClass("MGA", b"\x13"),
    MessageClass("LOG", b"\x21"),
    MessageClass("SEC", b"\x27"),
    MessageClass("HNR", b"\x28"),
]
"""UBX message classes."""


# Insert message classes into module namespace
for message_class in classes:
    globals()[message_class.name] = message_class


def get_by_name(name):
    """Obtain the message class with the given name.

    Raises a ValueError if no message class matches the given name.
    """
    for message_class in classes:
        if message_class.name==name:
            return message_class
    raise ValueError("Unknown MessageClass of name \"{}\".".format(name))


def get_by_byte(byte):
    """Obtain the message class with the given byte.

    Raises a ValueError if no message class matches the given byte.
    """
    if not isinstance(byte, bytes):
        raise TypeError("Expected byte argument to be of type \"bytes\" but it is \"{}\".".format(type(byte)))
    for message_class in classes:
        if message_class.byte==byte:
            return message_class
    raise ValueError("Unknown MessageClass with byte \"0x{}\".".format(utils.byte2hexstring(byte)))
