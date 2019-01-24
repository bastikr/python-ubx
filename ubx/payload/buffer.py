from .exceptions import PayloadError


class Buffer(object):
    __slots__ = "data", "index"

    def __init__(self, data, index):
        self.data = data
        self.index = index

    @property
    def remaining_bytesize(self):
        return len(self.data) - self.index

    def reset(self):
        self.index = 0

    def read(self, n):
        selection = self.data[self.index:self.index+n]
        self.index += n
        return selection

    def check_bytesize(self, bytesize, name, context):
        if bytesize is not None and self.remaining_bytesize < bytesize:
            raise PayloadError("Not enough remaining bytes ({}) to parse {} of size {}".format(
                    self.remaining_bytesize, name, bytesize),
                                self, context)
