from ..payload import *
from ..message import *


payload_description = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("fillLevel", U2),
    ("dropsAll", U2),
    ("dropsSinceMon", U2),
    ("nextMsgCnt", U2)
)

description = MessageDescription(
    name="MON-BATCH",
    message_class=b"\x0a",
    message_id=b"\x32",
    payload_description=Options(
        Empty,
        payload_description
    )
)
