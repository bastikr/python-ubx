from .payload.buffer import Buffer
from .payload.exceptions import PayloadError


class Parser:
    def __init__(self, *descriptions):
        self.descriptions = {}
        for d in descriptions:
            self.add_description(d)

    def add_description(self, description):
        self.descriptions[description.key] = description

    def parse(self, rawmsg):
        key = rawmsg.key
        if key not in self.descriptions:
            raise KeyError("No description for " + str(rawmsg))
        else:
            buffer = Buffer(rawmsg.payload, index=0)
            msg = self.descriptions[key].parse(buffer)
            if buffer.remaining_bytesize != 0:
                raise PayloadError("Not all bytes used.", buffer, None)
            return msg
