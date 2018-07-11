from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("type", U1),
    ("version", U1),
    ("infoCode", U1),
    ("msgId", U1),
    ("msgPayloadStart", 4*U1)
)

description = MessageDescription(
    message_class=MGA,
    message_id=MessageId("ACK", b"\x60"),
    payload_description=Options(
        payload_description
    )
)
