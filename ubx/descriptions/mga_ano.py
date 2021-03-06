from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("type", U1),
    ("version", U1),
    ("svId", U1),
    ("gnssId", U1),
    ("year", U1),
    ("month", U1),
    ("day", U1),
    ("reserved1", U1),
    ("data", 64*U1),
    ("reserved2", 4*U1)
)

description = MessageDescription(
    message_class=MGA,
    message_id=MessageId("ANO", b"\x20"),
    payload_description=Options(
        payload_description
    )
)
