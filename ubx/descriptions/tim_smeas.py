from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


flags = Bitfield(1, entries=[
    BitfieldEntry("freqValid", 0),
    BitfieldEntry("phaseValid", 1),
])

meas = Fields(
    ("sourceId", U1),
    ("flags", flags),
    ("phaseOffsetFrac", I1),
    ("phaseUncFrac", U1),
    ("phaseOffset", I4),
    ("phaseUnc", U4),
    ("reserved3", 4*U1),
    ("freqOffset", I4),
    ("freqUnc", U4)
)

payload_description = Fields(
    ("version", U1),
    ("numMeas", U1),
    ("reserved1", 2*U1),
    ("iTOW", U4),
    ("reserved2", 4*U1),
    ("meass", KeyLoop("numMeas", meas))
)

description = MessageDescription(
    message_class=TIM,
    message_id=MessageId("SMEAS", b"\x13"),
    payload_description=Options(
        Empty,
        payload_description
    )
)
