from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("iTOW", U4),
)

description = MessageDescription(
    name="NAV-EOE",
    message_class=b"\x01",
    message_id=b"\x61",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
