from ..payload import *
from ..message import *


flags = Bitfield(1, entries=[
    BitfieldEntry("useODO", 0),
    BitfieldEntry("useCOG", 1),
    BitfieldEntry("outLPVel", 2),
    BitfieldEntry("outLPCog", 3)
])

odoCfg = Bitfield(1, entries=[
    BitfieldEntry("profile", slice(0, 3)),
])

payload_description0 = Fields(
    ("version", U1),
    ("reserved1", List(3*[U1])),
    ("flags", flags),
    ("odoCfg", odoCfg),
    ("reserved2", List(6*[U1])),
    ("cogMaxSpeed", U1),
    ("cogMaxPosAcc", U1),
    ("reserved3", List(2*[U1])),
    ("velLpGain", U1),
    ("cogLpGain", U1),
    ("reserved4", List(2*[U1]))
)

description = MessageDescription(
    name="CFG-ODO",
    message_class=b"\x06",
    message_id=b"\x1e",
    payload_description=Options(
        Empty,
        payload_description0
    )
)
