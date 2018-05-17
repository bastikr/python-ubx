from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("reserved1", U1),
    ("lpMode", U1)
)

description = MessageDescription(
    name="CFG-RXM",
    message_class=b"\x06",
    message_id=b"\x11",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
