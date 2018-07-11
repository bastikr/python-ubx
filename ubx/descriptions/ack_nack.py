from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("clsID", U1),
    ("msgID", U1)
)

description = MessageDescription(
    message_class=ACK,
    message_id=MessageId("NACK", b"\x00"),
    payload_description=payload_description0
)
