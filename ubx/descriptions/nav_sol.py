from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


flags = Bitfield(1, entries=[
    BitfieldEntry("gnssFixOK", 0),
    BitfieldEntry("diffSoln", 1),
    BitfieldEntry("WKNSET", 2),
    BitfieldEntry("TOWSET", 3)
])

payload_description0 = Fields(
    ("iTOW", U4),
    ("fTOW", I4),
    ("week", I2),
    ("gpsFix", U1),
    ("flags", flags),
    ("ecefX", I4),
    ("ecefY", I4),
    ("ecefZ", I4),
    ("pAcc", U4),
    ("ecefVX", I4),
    ("ecefVY", I4),
    ("ecefVZ", I4),
    ("sAcc", U4),
    ("pDOP", U2),
    ("reserved1", U1),
    ("numSv", U1),
    ("reserved2", 4*U1)
)

description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("SOL", b"\x06"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
