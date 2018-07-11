from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("reserved1", U1),
    ("lpMode", U1)
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("RXM", b"\x11"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
