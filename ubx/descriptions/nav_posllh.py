from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("iTOW", U4),
    ("lon", I4),
    ("lat", I4),
    ("height", I4),
    ("hMSL", I4),
    ("hAcc", U4),
    ("vAcc", U4)
)

description = MessageDescription(
    name="NAV-POSLLH",
    message_class=b"\x01",
    message_id=b"\x02",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
