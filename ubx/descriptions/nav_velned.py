from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("iTOW", U4),
    ("velN", I4),
    ("velE", I4),
    ("velD", I4),
    ("speed", U4),
    ("gSpeed", U4),
    ("heading", I4),
    ("sAcc", U4),
    ("cAcc", U4)
)

description = MessageDescription(
    name="NAV-VELNED",
    message_class=b"\x01",
    message_id=b"\x12",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
