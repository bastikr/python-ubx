import binascii

template = """Statistics:
  Bytes read: {bytes_read_success}
  Checksum errors: {checksumerrors}
  Raw Messages: {rawmessages}
  Unknown Messages: {unknownmessages}
  Known Messages: {messages}
  Payload Errors: {payloaderrors}"""

def keystring(key):
    assert len(key)==2
    return "0x{} 0x{}".format(binascii.hexlify(key[0:1]).decode("utf-8"),
                              binascii.hexlify(key[1:2]).decode("utf-8"))

class MessageCounter:
    def __init__(self):
        self.data = {}

    def add(self, message):
        key = (message.key, message.name)
        if key in self.data:
            self.data[key] += 1
        else:
            self.data[key] = 1

    def __len__(self):
        n = 0
        for value in self.data.values():
            n += value
        return n

    def __str__(self):
        items = ["{"]
        items += ["{} ({}): {}".format(
                    key[1],
                    keystring(key[0]),
                    value) for key, value in self.data.items()]
        items += ["}"]
        return "\n".join(items)


class RawMessageCounter:
    def __init__(self):
        self.data = {}

    def add(self, rawmessage):
        key = rawmessage.key
        if key in self.data:
            self.data[key] += 1
        else:
            self.data[key] = 1

    def __len__(self):
        n = 0
        for value in self.data.values():
            n += value
        return n

    def __str__(self):
        items = ["{"]
        items += ["{}: {}".format(keystring(key), value) for key, value in self.data.items()]
        items += ["}"]
        return "\n".join(items)


class Statistics:
    def __init__(self):
        self.checksumerrors = 0

        self.rawmessages = RawMessageCounter()
        self.unknownmessages = RawMessageCounter()
        self.payloaderrors = MessageCounter()
        self.messages = MessageCounter()

        self.bytes_read_try = 0
        self.bytes_read_success = 0

    def add_checksumerror(self):
        self.checksumerrors += 1

    def add_rawmessage(self, rawmessage):
        self.rawmessages.add(rawmessage)

    def add_payloaderror(self, message):
        self.payloaderrors.add(message)

    def add_message(self, message):
        self.messages.add(message)

    def add_unknownmessage(self, rawmessage):
        self.unknownmessages.add(rawmessage)

    def add_bytesread_try(self, n):
        self.bytes_read_try += n

    def add_bytesread_success(self, n):
        self.bytes_read_success += n

    def __str__(self):
        return template.format(
            bytes_read_success = self.bytes_read_success,
            checksumerrors = self.checksumerrors,
            rawmessages = str(len(self.rawmessages)),
            unknownmessages = str(self.unknownmessages).replace("\n", "\n    "),
            messages = str(self.messages).replace("\n", "\n    "),
            payloaderrors = str(self.payloaderrors).replace("\n", "\n    "),
        )