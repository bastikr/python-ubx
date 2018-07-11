from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("iTOW", U4),
    ("lon", I4),
    ("lat", I4),
    ("height", I4),
    ("hMSL", I4),
    ("lonHp", I1),
    ("latHp", I1),
    ("heightHp", I1),
    ("hMSLHp", I1),
    ("hAcc", U4),
    ("vAcc", U4)
)

description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("HPPOSLLH", b"\x14"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
