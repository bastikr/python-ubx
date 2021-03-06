from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("entryIndex", U4),
    ("version", U1),
    ("reserved1", U1),
    ("year", U2),
    ("month", U1),
    ("day", U1),
    ("hour", U1),
    ("minute", U1),
    ("second", U1),
    ("reserved2", U1),
    ("byteCount", U2),
    ("bytes", KeyLoop("byteCount", U1))
)

description = MessageDescription(
    message_class=LOG,
    message_id=MessageId("RETRIEVESTRING", b"\x0d"),
    payload_description=Options(
        payload_description
    )
)
