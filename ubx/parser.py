from . import payload

class Parser:
    def __init__(self, *descriptions):
        self.descriptions = {}
        for d in descriptions:
            self.add_description(d)

    def add_description(self, description):
        key = description.message_class + description.message_id
        self.descriptions[key] = description

    def parse(self, rawmsg):
        key = rawmsg.message_class + rawmsg.message_id
        if key not in self.descriptions:
            raise KeyError("No description for " + str(rawmsg))
        else:
            buffer = payload.Buffer(rawmsg.payload, index=0)
            return self.descriptions[key].parse(buffer)
