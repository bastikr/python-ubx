from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("iTOW", U4),
    ("clkB", I4),
    ("clkD", I4),
    ("tAcc", U4),
    ("fAcc", U4)
)

description = MessageDescription(
    name="NAV-CLOCK",
    message_class=b"\x01",
    message_id=b"\x22",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
