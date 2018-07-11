from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("svid", U1)
)

payload_description1 = Fields(
    ("svid", U4),
    ("week", U4),
)

payload_description2 = Fields(
    ("svid", U4),
    ("week", U4),
    ("dwrd", 8*U4)
)

description = MessageDescription(
    message_class=AID,
    message_id=MessageId("ALM", b"\x30"),
    payload_description=Options(
        Empty,
        payload_description0,
        payload_description1,
        payload_description2,
    )
)
