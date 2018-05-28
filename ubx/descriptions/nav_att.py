from ..classid import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("iTOW", U4),
    ("version", U1),
    ("reserved1", 3*U1),
    ("roll", I4),
    ("pitch", I4),
    ("heading", I4),
    ("accRoll", U4),
    ("accPitch", U4),
    ("accHeading", U4),
)

description = MessageDescription(
    name="NAV-ATT",
    message_class=NAV,
    message_id=b"\x05",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
