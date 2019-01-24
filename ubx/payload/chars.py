import codecs


class Chars:
    def __init__(self, bytesize, encoding="iso-8859-1"):
        self.bytesize = bytesize
        self.encoding = codecs.lookup(encoding)

    def parse(self, buffer, context=None):
        buffer.check_bytesize(self.bytesize, "Chars", context)
        if self.bytesize is None:
            bytestring = buffer.read(buffer.remaining_bytesize)
        else:
            bytestring = buffer.read(self.bytesize)
        return bytestring.decode(self.encoding)

    def serialize(self, content, context=None):
        return content.encode(self.encoding)

    def __str__(self):
        return "Chars({})".format(self.bytesize)
