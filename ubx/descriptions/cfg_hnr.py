from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("highNavRate", U1),
    ("reserved1", 3*U1),
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("HNR", b"\x5c"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
