import struct

from . import syncchars
from . import classid
from . import utils
from . import checksum


class RawMessage:
    length_struct = struct.Struct("<H")

    def __init__(self, classbyte, idbyte, payload):
        assert len(classbyte) == 1
        assert len(idbyte) == 1
        try:
            self.message_class = classid.get_by_byte(classbyte)
        except ValueError:
            self.message_class = classid.ClassId("?", classbyte)
        self.message_id = idbyte
        self.payload = payload

    def __str__(self):
        template = "RawMessage(class=0x{}, id=0x{}, length={})"
        return template.format(
            utils.byte2hexstring(self.message_class.byte),
            utils.byte2hexstring(self.message_id),
            len(self.payload))

    def __len__(self):
        return len(self.payload)

    @property
    def key(self):
        return self.message_class + self.message_id

    @property
    def lengthbytes(self):
        return self.length_struct.pack(len(self))

    def checksum(self):
        return checksum.Checksum.from_bytestrings(
            self.message_class.byte,
            self.message_id,
            self.lengthbytes,
            self.payload)

    def serialize(self):
        data = [
            syncchars.CHAR1,
            syncchars.CHAR2,
            self.message_class.byte,
            self.message_id,
            self.lengthbytes,
            self.payload,
            self.checksum().bytes()
        ]
        return b"".join(data)
