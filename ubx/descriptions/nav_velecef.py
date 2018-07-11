from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("iTOW", U4),
    ("ecefVX", I4),
    ("ecefVY", I4),
    ("ecefVZ", I4),
    ("sAcc", U4)
)

description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("VELECEF", b"\x11"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
