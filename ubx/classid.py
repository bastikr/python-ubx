class ClassId:
    def __init__(self, name, classbyte):
        self.name = name
        self.classbyte = classbyte

NAV = ClassId("NAV", b"\x01")
RXM = ClassId("RXM", b"\x02")
INF = ClassId("INF", b"\x04")
ACK = ClassId("ACK", b"\x05")
CFG = ClassId("CFG", b"\x06")
UPD = ClassId("UPD", b"\x09")
MON = ClassId("MON", b"\x0a")
AID = ClassId("AID", b"\x0b")
TIM = ClassId("TIM", b"\x0d")
ESF = ClassId("ESF", b"\x10")
MGA = ClassId("MGA", b"\x13")
LOG = ClassId("LOG", b"\x21")
SEC = ClassId("SEC", b"\x27")
HNR = ClassId("HNR", b"\x28")
