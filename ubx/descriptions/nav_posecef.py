from ..classid import *
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
    name="NAV-POSECEF",
    message_class=NAV,
    message_id=b"\x01",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
