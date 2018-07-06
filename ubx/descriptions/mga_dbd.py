from ..message_class import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("reserved1", 12*U1),
    ("data", MatchedLoop(U1))
)

description = MessageDescription(
    name="MGA-DBD",
    message_class=MGA,
    message_id=b"\x80",
    payload_description=Options(
        Empty,
        payload_description
    )
)
