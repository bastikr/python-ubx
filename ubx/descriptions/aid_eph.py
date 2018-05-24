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
    name="AID-EPH",
    message_class=b"\x0b",
    message_id=b"\x31",
    payload_description=Options(
        Empty,
        payload_description0,
        payload_description1,
        payload_description2,
    )
)
