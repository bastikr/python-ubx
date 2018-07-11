from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("state", U4),
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("PWR", b"\x57"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
