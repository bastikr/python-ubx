from collections import OrderedDict

from .payload_type import PayloadType
from .context import Context
from .exceptions import PayloadError


class Loop(PayloadType):
    __slots__ = "description",

    def __init__(self, description):
        self.description = description
        self.bytesize = None

    def iterations(self, buffer, context):
        raise NotImplementedError()

    def parse(self, buffer, context):
        n = self.iterations(buffer, context)
        data = []
        subcontext = Context.child(context, data)
        for i in range(n):
            try:
                data.append(self.description.parse(buffer, subcontext))
            except PayloadError as e:
                raise PayloadError("Loop description: Payload error in iteration {}/{}.".format(i+1, n),
                                   buffer, context, e)
        return data

    def serialize(self, content, context=None):
        subcontext = Context.child(context, content)
        data = []
        if not isinstance(content, (list, tuple)):
            raise PayloadError("Serialization error in loop: content must be list or tuple but is {}.".format(
                type(content)), content, context)
        try:
            for i, entry in enumerate(content):
                data.append(self.description.serialize(entry, subcontext))
        except PayloadError as e:
            raise PayloadError("Serialization error in loop iteration {}".format(i),
                content, context, e)

        return b"".join(data)


class MatchedLoop(Loop):
    def __init__(self, description):
        if description.bytesize is None:
            raise ValueError("Description of matched loop has to have a fixed byte size.")
        Loop.__init__(self, description)

    def iterations(self, buffer, context):
        n, m = divmod(buffer.remaining_bytesize, self.description.bytesize)
        if m!=0:
            raise PayloadError("Matched loop of content length {} doesn't match input of length{}".format(
                self.description.bytesize, buffer.remaining_bytesize), buffer, context)
        return n

    def __str__(self):
        return "MatchedLoop:\n| " +\
               str(self.description).replace("\n", "\n| ")


class KeyLoop(Loop):
    __slots__ = "key",

    def __init__(self, key, description):
        Loop.__init__(self, description)
        self.key = key

    def iterations(self, buffer, context):
        return context.data[self.key]

    def __str__(self):
        return "Loop(key=\"{}\"):\n| ".format(self.key) +\
               str(self.description).replace("\n", "\n| ")
