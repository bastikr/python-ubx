from .base import DescriptionPrinter

from .. import utils
from .. import payload
from .. import message


class RST(DescriptionPrinter):
    def print_MessageDescription(self, obj):
        template = ":name: {name}\n\n"\
                   ":class: 0x{class}\n\n"\
                   ":id: 0x{id}\n\n"\
                   ":payload:\n\n  {payload}"
        return template.format(**{
            "name": obj.name,
            "class": utils.byte2hexstring(obj.message_class.byte),
            "id": utils.byte2hexstring(obj.message_id.byte),
            "payload": self.print_dispatch(obj.payload_description).replace("\n", "\n  ")
            })


    def print_EmptyVariable(self, obj):
        return "`Empty`"

    def print_BitfieldEntry(self, obj):
        if isinstance(obj.bits, int):
            bits = str(obj.bits)
        elif isinstance(obj.bits, slice):
            bits = "{}:{}".format(obj.bits.start, obj.bits.stop)
        else:
            bits = str(obj.bits)
        return "{bits}: *{name}*".format(name=obj.name, bits=bits)

    def print_Bitfield(self, obj):
        header = "Bitfield({})".format(obj.bytesize)
        if obj.entries is None:
            return header
        return header + "\n\n" + "\n\n".join("  " + self.print_BitfieldEntry(entry) for entry in obj.entries)

    def print_AtomicVariable(self, obj):
        return obj.name

    def print_Chars(self, obj):
        return "Chars({})".format(obj.bytesize)

    def print_Fields(self, obj):
        description_string = lambda name, description: "  :{}:\n    {}".format(name, self.print_dispatch(description).replace("\n", "\n    "))
        description_strings = [description_string(name, description) for name, description in obj.items()]
        if obj.bytesize is None:
            sizestring = "?"
        else:
            sizestring = str(obj.bytesize)
        return "Fields(length=" + sizestring + ")\n\n" + "\n\n".join(description_strings)

    def print_List(self, obj):
        return "List\n\n  - " +\
               "\n\n  - ".join([self.print_dispatch(d).replace("\n", "\n    ")
                             for d in obj.descriptions])

    def print_MatchedLoop(self, obj):
        return "MatchedLoop\n\n  " + self.print_dispatch(obj.description).replace("\n", "\n  ")

    def print_KeyLoop(self, obj):
        return "KeyLoop(key=\"{}\"):\n\n ".format(obj.key) +\
               self.print_dispatch(obj.description).replace("\n", "\n  ")

    def print_Options(self, obj):
        return "#. " + "\n\n#. ".join(self.print_dispatch(d).replace("\n", "\n     ") for d in obj.descriptions)
