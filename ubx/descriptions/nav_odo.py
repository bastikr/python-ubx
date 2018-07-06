from ..message_class import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("iTOW", U4),
    ("distance", U4),
    ("totalDistance", U4),
    ("distanceStd", U4)
)

description = MessageDescription(
    name="NAV-ODO",
    message_class=NAV,
    message_id=b"\x09",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
