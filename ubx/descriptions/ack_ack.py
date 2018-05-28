from ..classid import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("clsID", U1),
    ("msgID", U1)
)

description = MessageDescription(
    name="ACK-ACK",
    message_class=ACK,
    message_id=b"\x01",
    payload_description=payload_description0
)
