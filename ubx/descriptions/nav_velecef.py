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
    name="NAV-VELECEF",
    message_class=b"\x01",
    message_id=b"\x11",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
