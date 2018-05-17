from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("measRate", U2),
    ("navRate", U2),
    ("timeRef", U2),
)

description = MessageDescription(
    name="CFG-RATE",
    message_class=b"\x06",
    message_id=b"\x08",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
