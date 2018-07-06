from ..message_class import *
from ..payload import *
from ..message import *

# Request
payload_description0 = Fields(
    ("version", U1),
    ("type", U1),
    ("reserved1", 2*U1),
    ("year", U2),
    ("month", U1),
    ("day", U1),
    ("hour", U1),
    ("minute", U1),
    ("second", U1),
    ("reserved2", U1)
)

# Response
payload_description1 = Fields(
    ("version", U1),
    ("type", U1),
    ("reserved1", 2*U1),
    ("entryNumber", U4),
)

description = MessageDescription(
    name="LOG-FINDTIME",
    message_class=LOG,
    message_id=b"\x0e",
    payload_description=Options(
        payload_description0,
        payload_description1
    )
)
