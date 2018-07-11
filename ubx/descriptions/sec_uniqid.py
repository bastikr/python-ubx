from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("uniqueID", 5*U1),
)

description = MessageDescription(
    message_class=SEC,
    message_id=MessageId("UNIQID", b"\x03"),
    payload_description=Options(
        payload_description
    )
)
