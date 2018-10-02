from .. import payload
from .. import message


class DescriptionPrinter:
    def print_dispatch(self, obj):
        if isinstance(obj, message.MessageDescription):
            return self.print_MessageDescription(obj)
        if isinstance(obj, payload.EmptyVariable):
            return self.print_EmptyVariable(obj)
        if isinstance(obj, payload.BitfieldEntry):
            return self.print_BitfieldEntry(obj)
        if isinstance(obj, payload.Bitfield):
            return self.print_Bitfield(obj)
        if isinstance(obj, payload.AtomicVariable):
            return self.print_AtomicVariable(obj)
        if isinstance(obj, payload.Chars):
            return self.print_Chars(obj)
        if isinstance(obj, payload.Fields):
            return self.print_Fields(obj)
        if isinstance(obj, payload.List):
            return self.print_List(obj)
        if isinstance(obj, payload.MatchedLoop):
            return self.print_MatchedLoop(obj)
        if isinstance(obj, payload.KeyLoop):
            return self.print_KeyLoop(obj)
        if isinstance(obj, payload.Options):
            return self.print_Options(obj)
        raise NotImplementedError()

    def print_MessageDescription(self, obj):
        raise NotImplementedError()

    def print_EmptyVariable(self, obj):
        raise NotImplementedError()

    def print_BitfieldEntry(self, obj):
        raise NotImplementedError()

    def print_Bitfield(self, obj):
        raise NotImplementedError()

    def print_AtomicVariable(self, obj):
        raise NotImplementedError()

    def print_Chars(self, obj):
        raise NotImplementedError()

    def print_Fields(self, obj):
        raise NotImplementedError()

    def print_List(self, obj):
        raise NotImplementedError()

    def print_MatchedLoop(self, obj):
        raise NotImplementedError()

    def print_KeyLoop(self, obj):
        raise NotImplementedError()

    def print_Options(self, obj):
        raise NotImplementedError()
