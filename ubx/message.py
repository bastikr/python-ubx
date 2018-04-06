import struct
from . import checksum

syncchar1 = b"\xb5"
syncchar2 = b"\x62"

length_struct = struct.Struct("<H")

def lengthbytes(payload):
    length_struct.pack(len(payload))


class MessageDescription:
    def __init__(self, name, message_class, message_id, payload_description):
        self.name = name
        self.message_class = message_class
        self.message_id = message_id
        self.payload_description = payload_description

    def __str__(self):
        template = "MessageDescription:\n"\
                   "    name = {name}\n"\
                   "    class = 0x{class}\n"\
                   "    id = 0x{id}\n"\
                   "    payload = {payload}"
        return template.format(**{
                       "name" : self.name,
                       "class" : self.message_class.encode("hex"),
                       "id" : self.message_id.encode("hex"),
                       "payload" : str(self.payload_description).replace("\n", "\n"+" "*8)
                   })

    def parse(self, buffer):
        return Message(self, self.payload_description.parse(buffer))

    def serialize(self, content):
        payload = self.payload_description.serialize(content)
        data = [
            syncchar1,
            syncchar2,
            self.message_class,
            self.message_id,
            lengthbytes(payload),
            payload,
        ]
        return syncchar1 + syncchar2 + self.message_class + self.message_id


class Message:
    def __init__(self, description, content):
        self.description = description
        self.content = content

    def serialize(self):
        return self.description.serialize(self.content)

    def __str__(self):
        template = "Message(name=\"{}\")"
        return template.format(self.description.name)
