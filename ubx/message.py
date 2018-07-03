import struct
import codecs

from . import rawmessage
from . import classid


length_struct = struct.Struct("<H")


def lengthbytes(payload):
    length_struct.pack(len(payload))


class MessageDescription:
    def __init__(self, name, message_class, message_id, payload_description):
        assert isinstance(name, str)
        assert isinstance(message_class, classid.ClassId)
        assert isinstance(message_id, bytes)
        assert hasattr(payload_description, "parse")
        assert hasattr(payload_description, "serialize")
        self.name = name
        self.message_class = message_class
        self.message_id = message_id
        self.payload_description = payload_description

    @property
    def key(self):
        return self.message_class.classbyte + self.message_id

    def __str__(self):
        template = "MessageDescription:\n"\
                   "    name = {name}\n"\
                   "    class = 0x{class}\n"\
                   "    id = 0x{id}\n"\
                   "    payload = {payload}"
        return template.format(**{
            "name": self.name,
            "class": codecs.encode(self.message_class.classbyte, "hex").decode("utf-8"),
            "id": codecs.encode(self.message_id, "hex").decode("utf-8"),
            "payload": str(self.payload_description).replace("\n", "\n"+" "*8)
            })

    def parse(self, buffer):
        return Message(self, self.payload_description.parse(buffer))

    def rawmessage(self, content):
        return rawmessage.RawMessage(self.message_class.classbyte, self.message_id,
                                     self.payload_description.serialize(content))

    def serialize(self, content):
        return self.rawmessage(content).serialize()


class Message:
    def __init__(self, description, content):
        self.description = description
        self.content = content

    def serialize(self):
        return self.description.serialize(self.content)

    @property
    def name(self):
        return self.description.name

    @property
    def message_class(self):
        return self.description.message_class

    @property
    def message_id(self):
        return self.description.message_id

    @property
    def key(self):
        return self.message_class.classbyte + self.message_id

    def __str__(self):
        template = "Message(name=\"{}\")"
        return template.format(self.name)
