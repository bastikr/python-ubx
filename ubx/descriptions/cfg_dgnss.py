from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("dgnssMode", U1),
    ("reserved1", 3*U1),
)

description = MessageDescription(
    name="CFG-DGNSS",
    message_class=b"\x06",
    message_id=b"\x70",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
