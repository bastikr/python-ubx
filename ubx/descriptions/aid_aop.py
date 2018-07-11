from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("svid", U1),
)

payload_description1 = Fields(
    ("gnssId", U1),
    ("svId", U1),
    ("reserved1", 2*U1),
    ("data", 64*U1)
)

description = MessageDescription(
    message_class=AID,
    message_id=MessageId("AOP", b"\x33"),
    payload_description=Options(
        Empty,
        payload_description0,
        payload_description1
    )
)
