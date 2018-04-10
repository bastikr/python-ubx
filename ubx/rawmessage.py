import struct
from . import checksum


syncchar1 = b"\xb5"
syncchar2 = b"\x62"


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
                    self.message_class.encode("hex"),
                    self.message_id.encode("hex"),
                    len(self.payload)
                    )

    def __len__(self):
        return len(self.payload)

    @property
    def lengthbytes(self):
        return self.length_struct.pack(len(self))

    def checksum(self):
        return checksum.calculate(
                    self.message_class,
                    self.message_id,
                    self.lengthbytes,
                    self.payload
                    )

    def serialize(self):
        data = [
            syncchar1,
            syncchar2,
            self.message_class,
            self.message_id,
            self.lengthbytes,
            self.payload,
            self.checksum().bytes()
        ]
        return "".join(data)
