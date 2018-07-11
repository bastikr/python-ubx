from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("version", U1),
    ("powerSetupValue", U1),
    ("period", U2),
    ("onTime", U2),
    ("reserved1", 2*U1)
)


description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("PMS", b"\x86"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
