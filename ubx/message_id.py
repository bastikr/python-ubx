"""UBX message ids"""

from . import utils


class MessageId:
    """
    Simple class storing the name and byte of a UBX message id.
    """

    __slots__ = "name", "subname", "byte"

    def __init__(self, name, byte, subname=None):
        if not isinstance(byte, bytes):
            raise TypeError("byte argument has to be of type \"byte\" but is: {}".format(
                type(byte)))
        self.name = name
        self.subname = subname
        self.byte = byte

    def __eq__(self, other):
        if isinstance(other, MessageId):
            return self.name==other.name\
               and self.subname==other.subname\
               and self.byte==other.byte
        else:
            return NotImplemented

    def __ne__(self, other):
        return not self==other

    def __str__(self):
        bytestring = utils.byte2hexstring(self.byte)
        if self.subname is None:
            return "MessageId(name={}, byte=0x{})".format(self.name, bytestring)
        else:
            return "MessageId(name={}, subname={}, byte=0x{})".format(
                self.name, self.subname, bytestring)
