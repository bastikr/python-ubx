from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("state", U4),
)

description = MessageDescription(
    name="CFG-PWR",
    message_class=b"\x06",
    message_id=b"\x57",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
