from ..message_class import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("seedHi", U4),
    ("seedLo", U4),
)

description = MessageDescription(
    name="CFG-DYNSEED",
    message_class=CFG,
    message_id=b"\x85",
    payload_description=Options(
        payload_description0,
    )
)
