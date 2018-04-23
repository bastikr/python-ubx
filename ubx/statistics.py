import binascii

template = """Statistics:
  Bytes read: {bytes_read_success}
  Unknown Messages: {unknown_messages}
  Known Messages: {known_messages}
  Errors: {error}"""

def keystring(key):
    assert len(key)==2
    return "0x{} 0x{}".format(binascii.hexlify(key[0:1]).decode("utf-8"),
                              binascii.hexlify(key[1:2]).decode("utf-8"))

class MessageCounter:
    def __init__(self):
        self.data = {}

    def add(self, key):
        if key in self.data:
            self.data[key] += 1
        else:
            self.data[key] = 1

    def __str__(self):
        items = ["{"]
        items += ["{}: {}".format(keystring(key), value) for key, value in self.data.items()]
        items += ["}"]
        return "\n".join(items)


class Statistics:
    def __init__(self):
        self.success = 0
        self.error = 0
        self.unknown_messages = MessageCounter()
        self.known_messages = MessageCounter()
        self.bytes_read_try = 0
        self.bytes_read_success = 0

    def add_error(self):
        self.error += 1

    def add_success(self):
        self.success += 1

    def add_knownmessage(self, message):
        self.add_success()
        self.known_messages.add(message.key)

    def add_unknownmessage(self, message):
        self.add_success()
        self.unknown_messages.add(message.key)

    def add_bytesread_try(self, n):
        self.bytes_read_try += n

    def add_bytesread_success(self, n):
        self.bytes_read_success += n

    def __str__(self):
        return template.format(
            bytes_read_success = self.bytes_read_success,
            error = self.error,
            unknown_messages = str(self.unknown_messages).replace("\n", "\n    "),
            known_messages = str(self.known_messages).replace("\n", "\n    "),
        )