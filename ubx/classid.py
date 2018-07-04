from . import utils


class ClassId:
    def __init__(self, name, classbyte):
        self.name = name
        self.classbyte = classbyte

    def __eq__(self, other):
        if isinstance(other, ClassId):
            return self.name==other.name and self.classbyte==other.classbyte
        else:
            return NotImplemented

    def __ne__(self, other):
        return not self==other


ids = [
    ClassId("NAV", b"\x01"),
    ClassId("RXM", b"\x02"),
    ClassId("INF", b"\x04"),
    ClassId("ACK", b"\x05"),
    ClassId("CFG", b"\x06"),
    ClassId("UPD", b"\x09"),
    ClassId("MON", b"\x0a"),
    ClassId("AID", b"\x0b"),
    ClassId("TIM", b"\x0d"),
    ClassId("ESF", b"\x10"),
    ClassId("MGA", b"\x13"),
    ClassId("LOG", b"\x21"),
    ClassId("SEC", b"\x27"),
    ClassId("HNR", b"\x28"),
]

for id in ids:
    globals()[id.name] = id

def get_by_name(name):
    for id in ids:
        if id.name==name:
            return id
    raise ValueError("Unknown ClassId of name \"{}\".".format(name))

def get_by_byte(byte, defaultname=None):
    if not isinstance(byte, bytes):
        raise TypeError("Expected byte argument to be of type \"bytes\" but it is \"{}\".".format(type(byte)))
    for id in ids:
        if id.classbyte==byte:
            return id
    if defaultname is None:
        raise ValueError("Unknown ClassId with byte \"0x{}\".".format(utils.byte2hexstring(byte)))
    return ClassId(defaultname, byte)
