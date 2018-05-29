from ..classid import *
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
    ("reserved2", 3*U1),
    ("distance", U4),
    ("reserved3", 12*U1)
)

description = MessageDescription(
    name="LOG-RETRIEVEPOSEXTRA",
    message_class=LOG,
    message_id=b"\x0f",
    payload_description=Options(
        payload_description
    )
)
