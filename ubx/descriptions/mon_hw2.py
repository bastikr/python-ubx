from ..message_class import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("ofsI", I1),
    ("magI", U1),
    ("ofsQ", I1),
    ("magQ", U1),
    ("cfgSource", U1),
    ("reserved1", 3*U1),
    ("lowLevCfg", U4),
    ("reserved2", 8*U1),
    ("postStatus", U4),
    ("reserved3", 4*U1)
)

description = MessageDescription(
    name="MON-HW2",
    message_class=MON,
    message_id=b"\x0b",
    payload_description=Options(
        Empty,
        payload_description
    )
)
