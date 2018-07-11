from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


fences = Fields(
    ("lat", I4),
    ("lon", I4),
    ("radius", U4)
)

payload_description0 = Fields(
    ("version", U1),
    ("numFences", U1),
    ("confLvl", U1),
    ("reserved1", U1),
    ("pioEnabled", U1),
    ("pinPolarity", U1),
    ("pin", U1),
    ("reserved2", U1),
    ("fences", KeyLoop("numFences", fences))
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("GEOFENCE", b"\x69"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
