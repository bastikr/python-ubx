from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("startNumber", U4),
    ("entryCount", U4),
    ("version", U1),
    ("reserved1", 3*U1)
)

description = MessageDescription(
    message_class=LOG,
    message_id=MessageId("RETRIEVE", b"\x09"),
    payload_description=Options(
        payload_description
    )
)
