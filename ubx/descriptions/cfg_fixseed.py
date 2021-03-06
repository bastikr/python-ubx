from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


ids = Fields(
    ("classId", U1),
    ("msgId", U1),
)

payload_description0 = Fields(
    ("version", U1),
    ("length", U1),
    ("reserved1", 2*U1),
    ("seedHi", U4),
    ("seedLo", U4),
    ("ids", KeyLoop("length", ids))
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("FIXSEED", b"\x84"),
    payload_description=Options(
        payload_description0,
    )
)
