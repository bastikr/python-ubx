from ..payload import *
from ..message import *


fence = Fields(
    ("state", U1),
    ("reserved1", U1)
)

payload_description0 = Fields(
    ("iTOW", U4),
    ("version", U1),
    ("status", U1),
    ("numFences", U1),
    ("combState", U1),
    ("fences", KeyLoop("numFences", fence))
)

description = MessageDescription(
    name="NAV-GEOFENCE",
    message_class=b"\x01",
    message_id=b"\x39",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
