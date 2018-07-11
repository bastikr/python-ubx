from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


valid = Bitfield(1, entries=[
    BitfieldEntry("sowValid", 0),
    BitfieldEntry("weekValid", 1),
    BitfieldEntry("leapSValid", 2),
])

payload_description0 = Fields(
    ("iTOW", U4),
    ("SOW", U4),
    ("fSOW", I4),
    ("week", I2),
    ("leapS", I1),
    ("valid", valid),
    ("tAcc", U4)
)

description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("TIMEDBS", b"\x24"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
