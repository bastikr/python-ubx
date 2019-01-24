class PayloadType(object):
    __slots__ = "bytesize",

    def parse(self, buffer, context=None):
        raise NotImplementedError()

    def serialize(self, content, context=None):
        raise NotImplementedError()

