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
    name="CFG-PMS",
    message_class=b"\x06",
    message_id=b"\x86",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
