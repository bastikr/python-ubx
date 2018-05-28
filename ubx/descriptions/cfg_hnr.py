from ..classid import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("highNavRate", U1),
    ("reserved1", 3*U1),
)

description = MessageDescription(
    name="CFG-HNR",
    message_class=CFG,
    message_id=b"\x5c",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
