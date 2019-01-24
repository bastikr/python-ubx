from collections import OrderedDict

from .context import Context
from .exceptions import PayloadError


class Fields(OrderedDict):
    def __init__(self, *fields):
        OrderedDict.__init__(self, fields)
        bytesize = 0
        for _, description in fields:
            if not hasattr(description, "bytesize") or description.bytesize is None:
                bytesize = None
                break
            else:
                bytesize += description.bytesize
        self.bytesize = bytesize

    def parse(self, buffer, context=None):
        buffer.check_bytesize(self.bytesize, "Fields", context)
        data = OrderedDict()
        subcontext = Context.child(context, data)
        for name, description in self.items():
            try:
                data[name] = description.parse(buffer, subcontext)
            except PayloadError as e:
                raise PayloadError("Fields: PayloadError while parsing the field {}.".format(name),
                                   buffer, context, e)
        return data

    def serialize(self, content, context=None):
        if not isinstance(content, (dict, OrderedDict)):
            raise PayloadError("Serialization error in Fields: content must be dict or OrderedDict but is {}.".format(
                type(content)), content, context)
        if len(content) != len(self):
            raise PayloadError("Serialization error in Fields: length of content is {} instead of {}.".format(
                len(content), len(self)), content, context)
        subcontext = Context.child(context, content)
        data = []
        for name, description in self.items():
            if name not in content:
                raise PayloadError("Serialization error in Fields: content has no field with name {}.".format(name),
                    content, context)
            try:
                data.append(description.serialize(content[name], subcontext))
            except PayloadError as e:
                raise PayloadError("Serialization error in field {}.".format(name),
                    content, context, e)
        return b"".join(data)

    def __str__(self):
        description_strings = []
        for name, description in self.items():
            description_string = str(description)
            if "\n" in description_string:
                description_string = description_string.replace("\n", "\n    ")
                description_strings.append("{}:\n    {}".format(name, description_string))
            else:
                description_strings.append("{}: {}".format(name, description_string))
        if self.bytesize is None:
            sizestring = "?"
        else:
            sizestring = str(self.bytesize)
        return "Fields(length=" + sizestring + ") {\n  " + ",\n  ".join(description_strings) + "\n}"
