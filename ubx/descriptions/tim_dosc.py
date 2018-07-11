from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("value", U4)
)

description = MessageDescription(
    message_class=TIM,
    message_id=MessageId("DOSC", b"\x11"),
    payload_description=Options(
        payload_description
    )
)
