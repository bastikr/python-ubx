from .context import Context
from .exceptions import PayloadError


class Options:
    def __init__(self, *descriptions):
        self.descriptions = descriptions

    def parse(self, buffer, context=None):
        payload_errors = []
        for description in self.descriptions:
            if description.bytesize is not None and buffer.remaining_bytesize != description.bytesize:
                payload_errors.append(PayloadError(
                    "Description bytesize ({}) doesn't match remaining bytesize ({})".format(
                        description.bytesize, buffer.remaining_bytesize),
                    buffer, context))
                continue
            try:
                return description.parse(buffer, context)
            except PayloadError as e:
                payload_errors.append(e)
                buffer.reset()
                continue
        raise PayloadError("All available description options failed.",
                           buffer, context, payload_errors)

    def serialize(self, content, context=None):
        payload_errors = []
        subcontext = Context.child(context, content)
        for description in self.descriptions:
            try:
                return description.serialize(content, subcontext)
            except PayloadError as e:
                payload_errors.append(e)
        raise PayloadError("All available description options failed.",
                           content, context, payload_errors)

    def __str__(self):
        options = []
        for i, d in enumerate(self.descriptions):
            options.append("  [{}]: ".format(i) + str(d).replace("\n", "\n    "))
        return "Options:\n" + "\n".join(options)
