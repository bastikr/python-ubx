from ..payload import *
from ..message import *


flags = Bitfield(1, entries=[
    BitfieldEntry("channel", slice(0, 4)),
    BitfieldEntry("dgpsUsed", 4)
])

ch = Fields(
    ("svid", U1),
    ("flags", flags),
    ("ageC", U2),
    ("prc", R4),
    ("prrc", R4)
)

payload_description0 = Fields(
    ("iTOW", U4),
    ("age", I4),
    ("baseId", I2),
    ("baseHealth", I2),
    ("numCh", U1),
    ("status", U1),
    ("reserved1", 2*U1),
    ("chs", KeyLoop("numCh", ch))
)

description = MessageDescription(
    name="NAV-DGPS",
    message_class=b"\x01",
    message_id=b"\x31",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
