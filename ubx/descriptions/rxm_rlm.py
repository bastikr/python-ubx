from ..classid import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("version", U1),
    ("type", U1),
    ("svId", U1),
    ("reserved1", U1),
    ("beacon", 8*U1),
    ("message", U1),
    ("params", 2*U1),
    ("reserved2", U1)
)

payload_description1 = Fields(
    ("version", U1),
    ("type", U1),
    ("svId", U1),
    ("reserved1", U1),
    ("beacon", 8*U1),
    ("message", U1),
    ("params", 12*U1),
    ("reserved2", 3*U1)
)

description = MessageDescription(
    name="RXM-RLM",
    message_class=RXM,
    message_id=b"\x59",
    payload_description=Options(
        Empty,
        payload_description0,
        payload_description1
    )
)
