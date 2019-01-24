from .payload_type import PayloadType
from .context import Context
from .exceptions import PayloadError


class List(PayloadType):
    __slots__ = "descriptions",

    def __init__(self, descriptions):
        self.descriptions = descriptions
        bytesize = 0
        for description in descriptions:
            if not hasattr(description, "bytesize") or description.bytesize is None:
                bytesize = None
                break
            else:
                bytesize += description.bytesize
        self.bytesize = bytesize

    def parse(self, buffer, context=None):
        buffer.check_bytesize(self.bytesize, "List", context)
        data = []
        subcontext = Context.child(context, data)
        for i, description in enumerate(self.descriptions):
            try:
                data.append(description.parse(buffer, subcontext))
            except PayloadError as e:
                raise PayloadError("List description: PayloadError while parsing entry number {}.".format(i),
                                   buffer, context, e)
        return data

    def serialize(self, content, context=None):
        if not isinstance(content, (list, tuple)):
            raise PayloadError("Serialization error in list: content must be list or tuple but is {}.".format(
                type(content)), content, context)
        if len(content) != len(self.descriptions):
            raise PayloadError("Serialization error in list: length of content is {} instead of {}.".format(
                len(content), len(self.descriptions)), content, context)
        subcontext = Context.child(context, content)
        data = []
        for i, description in enumerate(self.descriptions):
            try:
                data.append(description.serialize(content[i], subcontext))
            except PayloadError as e:
                raise PayloadError("Serialization error in list entry number {}".format(i),
                    content, context, e)
        return b"".join(data)

    def __str__(self):
        return "[\n  " +\
               ",\n  ".join([str(d).replace("\n", "\n  ")
                             for d in self.descriptions]) +\
               "\n]"
