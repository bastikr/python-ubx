import struct

from . import syncchars
from . import utils
from . import checksum


class RawMessage:
    length_struct = struct.Struct("<H")

    def __init__(self, message_class, message_id, payload):
        assert len(message_class) == 1
        assert len(message_id) == 1
        self.message_class = message_class
        self.message_id = message_id
        self.payload = payload

    def __str__(self):
        template = "RawMessage(class=0x{}, id=0x{}, length={})"
        return template.format(
            utils.byte2hexstring(self.message_class.classbyte),
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
            self.message_class,
            self.message_id,
            self.lengthbytes,
            self.payload)

    def serialize(self):
        data = [
            syncchars.CHAR1,
            syncchars.CHAR2,
            self.message_class,
            self.message_id,
            self.lengthbytes,
            self.payload,
            self.checksum().bytes()
        ]
        return b"".join(data)
