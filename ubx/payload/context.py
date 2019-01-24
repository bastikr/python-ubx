class Context(object):
    __slots__ = "data", "parent"

    def __init__(self, data=None, parent=None):
        self.data = data
        self.parent = parent

    @staticmethod
    def child(context, data):
        return Context(data=data, parent=context)
