from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("svid", U1)
)

payload_description1 = Fields(
    ("svid", U4),
    ("how", U4),
)

payload_description2 = Fields(
    ("svid", U4),
    ("how", U4),
    ("sf1d", 8*U4),
    ("sf2d", 8*U4),
    ("sf3d", 8*U4)
)

description = MessageDescription(
    message_class=AID,
    message_id=MessageId("EPH", b"\x31"),
    payload_description=Options(
        Empty,
        payload_description0,
        payload_description1,
        payload_description2,
    )
)
