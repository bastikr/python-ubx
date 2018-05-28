from ..classid import *
from ..payload import *
from ..message import *


valid = Bitfield(1, entries=[
    BitfieldEntry("validTOW", 0),
    BitfieldEntry("validWKN", 1),
    BitfieldEntry("validUTC", 1),
    BitfieldEntry("utcStandard", slice(4, 8))
])

payload_description0 = Fields(
    ("iTOW", U4),
    ("tAcc", U4),
    ("nano", I4),
    ("year", U2),
    ("month", U1),
    ("day", U1),
    ("hour", U1),
    ("min", U1),
    ("sec", U1),
    ("valid", valid),
)

description = MessageDescription(
    name="NAV-TIMEUTC",
    message_class=NAV,
    message_id=b"\x21",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
