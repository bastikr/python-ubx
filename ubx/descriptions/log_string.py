from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("bytes", MatchedLoop(U1))
)

description = MessageDescription(
    message_class=LOG,
    message_id=MessageId("STRING", b"\x04"),
    payload_description=Options(
        payload_description
    )
)
