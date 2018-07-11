from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


flags = Bitfield(2, entries=[
    BitfieldEntry("lla", 0),
    BitfieldEntry("altInv", 1),
])

payload_description0 = Fields(
    ("timeMode", U1),
    ("reserved1", U1),
    ("flags", flags),
    ("ecefXOrLat", I4),
    ("ecefYOrLon", I4),
    ("ecefZOrAlt", I4),
    ("fixedPosAcc", U4),
    ("svinMinDur", U4),
    ("svinAccLim", U4)
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("TMODE2", b"\x3d"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
