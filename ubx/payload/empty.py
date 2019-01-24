from .payload_type import PayloadType
from .exceptions import PayloadError


class EmptyVariable(PayloadType):
    bytesize = 0

    def parse(self, buffer, context=None):
        return None

    def serialize(self, content, context=None):
        if content is not None:
            raise PayloadError("Content to be serialized by EmptyVariable is not None.", content, context)
        return b""

    def __str__(self):
        return "Empty"


Empty = EmptyVariable()
