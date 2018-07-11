from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("iTOW", U4),
    ("ecefX", I4),
    ("ecefY", I4),
    ("ecefZ", I4),
    ("pAcc", U4)
)

description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("POSECEF", b"\x01"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
