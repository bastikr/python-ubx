from ..message_class import *
from ..message_id import *
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
    message_class=NAV,
    message_id=MessageId("VELNED", b"\x12"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
