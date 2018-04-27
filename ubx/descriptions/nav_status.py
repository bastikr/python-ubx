from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("iTOW", U4),
    ("gpsFix", U1),
    ("flags", X1),
    ("fixStat", X1),
    ("flags2", X1),
    ("ttff", U4),
    ("msss", U4),
)

description = MessageDescription(
    name="NAV-STATUS",
    message_class=b"\x01",
    message_id=b"\x03",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
