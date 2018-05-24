from ..payload import *
from ..message import *


flags = Bitfield(2, entries=[
    BitfieldEntry("mode", slice(0, 8)),
    BitfieldEntry("lla", 8),
])

payload_description0 = Fields(
    ("version", U1),
    ("reserved1", U1),
    ("flags", flags),
    ("ecefXOrLat", I4),
    ("ecefYOrLon", I4),
    ("ecefZOrAlt", I4),
    ("ecefXOrLatHP", I1),
    ("ecefYOrLonHP", I1),
    ("ecefZOrAltHP", I1),
    ("reserved2", U1),
    ("fixedPosAcc", U4),
    ("svinMinDur", U4),
    ("svinAccLimit", U4),
    ("reserved3", 8*U1),
)

description = MessageDescription(
    name="CFG-TMODE3",
    message_class=b"\x06",
    message_id=b"\x71",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
