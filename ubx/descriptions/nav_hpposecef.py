from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("iTOW", U4),
    ("ecefX", I4),
    ("ecefY", I4),
    ("ecefZ", I4),
    ("ecefXHp", I1),
    ("ecefYHp", I1),
    ("ecefZHp", I1),
    ("reserved2", U1),
    ("pAcc", U4)
)

description = MessageDescription(
    name="NAV-HPPOSECEF",
    message_class=b"\x01",
    message_id=b"\x13",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
