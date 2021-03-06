from ..message_class import *
from ..message_id import *
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
    message_class=NAV,
    message_id=MessageId("CLOCK", b"\x22"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
