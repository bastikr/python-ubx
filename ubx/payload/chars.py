import codecs

from .payload_type import PayloadType


class Chars(PayloadType):
    __slots__ = "codec",

    def __init__(self, bytesize, encoding="iso-8859-1"):
        self.bytesize = bytesize
        self.codec = codecs.lookup(encoding)

    def parse(self, buffer, context=None):
        buffer.check_bytesize(self.bytesize, "Chars", context)
        if self.bytesize is None:
            bytestring = buffer.read(buffer.remaining_bytesize)
        else:
            bytestring = buffer.read(self.bytesize)
        return self.codec.decode(bytestring)

    def serialize(self, content, context=None):
        return self.codec.encode(content)

    def __str__(self):
        return "Chars({})".format(self.bytesize)
