from ..payload import *
from ..message import *


sensStatus1 = Bitfield(1, entries=[
    BitfieldEntry("type", slice(0, 6)),
    BitfieldEntry("used", 6),
    BitfieldEntry("ready", 7),
])

sensStatus2 = Bitfield(1, entries=[
    BitfieldEntry("calibStatus", slice(0, 2)),
    BitfieldEntry("timeStatus", slice(2, 4))
])

faults = Bitfield(1, entries=[
    BitfieldEntry("badMeas", 0),
    BitfieldEntry("badTTag", 1),
    BitfieldEntry("missingMeas", 2),
    BitfieldEntry("noisyMeas", 3),
])

sens = Fields(
    ("sensStatus1", sensStatus1),
    ("sensStatus2", sensStatus2),
    ("freq", U1),
    ("faults", faults)
)

payload_description0 = Fields(
    ("iTOW", U4),
    ("version", U1),
    ("reserved1", 7*U1),
    ("fusionMode", U1),
    ("reserved2", 2*U1),
    ("numSens", U1),
    ("sens", KeyLoop("numSens", sens))
)

description = MessageDescription(
    name="ESF-STATUS",
    message_class=b"\x10",
    message_id=b"\x10",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
