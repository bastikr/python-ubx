from ..message_class import *
from ..message_id import *
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
    message_class=MON,
    message_id=MessageId("BATCH", b"\x32"),
    payload_description=Options(
        Empty,
        payload_description
    )
)
