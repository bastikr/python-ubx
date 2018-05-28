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
    name="SEC-SIGN",
    message_class=b"\x27",
    message_id=b"\x01",
    payload_description=Options(
        payload_description
    )
)
