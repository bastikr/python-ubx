from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("classID", U1),
    ("messageID", U1),
    ("checksum", U2),
    ("hash", 32*U1)
)

description = MessageDescription(
    message_class=SEC,
    message_id=MessageId("SIGN", b"\x01"),
    payload_description=Options(
        payload_description
    )
)
