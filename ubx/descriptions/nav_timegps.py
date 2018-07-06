from ..message_class import *
from ..payload import *
from ..message import *


valid = Bitfield(1, entries=[
    BitfieldEntry("towValid", 0),
    BitfieldEntry("weekValid", 1),
    BitfieldEntry("leapSValid", 2),
])

payload_description0 = Fields(
    ("iTOW", U4),
    ("fTOW", I4),
    ("week", I2),
    ("leapS", I1),
    ("valid", valid),
    ("tAcc", U4)
)

description = MessageDescription(
    name="NAV-TIMEGPS",
    message_class=NAV,
    message_id=b"\x20",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
