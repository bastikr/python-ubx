from ..payload import *
from ..message import *


ids = Fields(
    ("classId", U1),
    ("msgId", U1),
)

payload_description0 = Fields(
    ("version", U1),
    ("length", U1),
    ("reserved1", List(2*[U1])),
    ("seedHi", U4),
    ("seedLo", U4),
    ("ids", KeyLoop("length", ids))
)

description = MessageDescription(
    name="CFG-FIXSEED",
    message_class=b"\x06",
    message_id=b"\x84",
    payload_description=Options(
        payload_description0,
    )
)
