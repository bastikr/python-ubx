from ..payload import *
from ..message import *


payload_description = Fields(
    ("msg1", 8*U2),
    ("msg2", 8*U2),
    ("msg3", 8*U2),
    ("msg4", 8*U2),
    ("msg5", 8*U2),
    ("msg6", 8*U2),
    ("skipped", 6*U4)
    
)

description = MessageDescription(
    name="MON-MSGPP",
    message_class=b"\x0a",
    message_id=b"\x06",
    payload_description=Options(
        Empty,
        payload_description
    )
)
