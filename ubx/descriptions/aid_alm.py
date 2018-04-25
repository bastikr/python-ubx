from ..payload import *
from ..message import *

payload_description0 = Fields()

payload_description1 = Fields(
    ("svid", U1)
)

payload_description2 = Fields(
    ("svid", U4),
    ("week", U4),
)

payload_description3 = Fields(
    ("svid", U4),
    ("week", U4),
    ("dwrd", List(8*[U4]))
)

description = MessageDescription(
    name = "AID-ALM",
    message_class = b"\x0b",
    message_id = b"\x30",
    payload_description = Options(
        payload_description0,
        payload_description1,
        payload_description2,
        payload_description3,
    )
)
