from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("reserved1", 12*U1),
    ("data", MatchedLoop(U1))
)

description = MessageDescription(
    message_class=MGA,
    message_id=MessageId("DBD", b"\x80"),
    payload_description=Options(
        Empty,
        payload_description
    )
)
