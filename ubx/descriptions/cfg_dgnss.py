from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("dgnssMode", U1),
    ("reserved1", 3*U1),
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("DGNSS", b"\x70"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
