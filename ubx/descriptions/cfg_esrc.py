from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


flags = Bitfield(2, [
    BitfieldEntry("polarity", 0),
    BitfieldEntry("gnssUtc", 1)
])

sources = Fields(
    ("extInt", U1),
    ("sourceType", U1),
    ("flags", flags),
    ("freq", U4),
    ("reserved2", 4*U1),
    ("withTemp", U4),
    ("withAge", U4),
    ("timeToTemp", U2),
    ("maxDevLifeTime", U2),
    ("offset", I4),
    ("offsetUncertainty", U4),
    ("jitter", U4),
)

payload_description0 = Fields(
    ("version", U1),
    ("numSources", U1),
    ("reserved1", 2*U1),
    ("sources", KeyLoop("numSources", sources))
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("ESRC", b"\x60"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
