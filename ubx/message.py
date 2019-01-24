import struct

from . import utils
from . import rawmessage
from .message_class import MessageClass
from .message_id import MessageId


class MessageDescription(object):
    __slots__ = "message_class", "message_id", "payload_description"

    def __init__(self, message_class, message_id, payload_description):
        assert isinstance(message_class, MessageClass)
        assert isinstance(message_id, MessageId)
        assert hasattr(payload_description, "parse")
        assert hasattr(payload_description, "serialize")
        self.message_class = message_class
        self.message_id = message_id
        self.payload_description = payload_description

    @property
    def name(self):
        return self.message_class.name + "-" + self.message_id.name

    @property
    def key(self):
        return self.message_class.byte + self.message_id.byte

    def __str__(self):
        template = "MessageDescription:\n"\
                   "    name = {name}\n"\
                   "    class = 0x{class}\n"\
                   "    id = 0x{id}\n"\
                   "    payload = {payload}"
        return template.format(**{
            "name": self.name,
            "class": utils.byte2hexstring(self.message_class.byte),
            "id": utils.byte2hexstring(self.message_id.byte),
            "payload": str(self.payload_description).replace("\n", "\n"+" "*8)
            })

    def parse(self, buffer):
        return Message(self, self.payload_description.parse(buffer))

    def rawmessage(self, content):
        return rawmessage.RawMessage(self.message_class.byte, self.message_id.byte,
                                     self.payload_description.serialize(content))

    def serialize(self, content):
        return self.rawmessage(content).serialize()


class Message(object):
    __slots__ = "description", "content"

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
        return self.message_class.byte + self.message_id.byte

    def __str__(self):
        template = "Message(name=\"{}\")"
        return template.format(self.name)
