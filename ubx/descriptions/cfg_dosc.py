from ..message_class import *
from ..payload import *
from ..message import *


flags = Bitfield(2, [
    BitfieldEntry("isCalibrated", 0),
    BitfieldEntry("controlIf", slice(1, 5))
])

osc = Fields(
    ("oscId", U1),
    ("reserved2", U1),
    ("flags", flags),
    ("freq", U4),
    ("phaseOffset", I4),
    ("withTemp", U4),
    ("withAge", U4),
    ("timeToTemp", U2),
    ("reserved3", 2*U1),
    ("gainVco", I4),
    ("gainUncertainty", U1),
    ("reserved4", 3*U1),
)

payload_description0 = Fields(
    ("version", U1),
    ("numOsc", U1),
    ("reserved1", 2*U1),
    ("osc", KeyLoop("numOsc", osc))
)

description = MessageDescription(
    name="CFG-DOSC",
    message_class=CFG,
    message_id=b"\x61",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
