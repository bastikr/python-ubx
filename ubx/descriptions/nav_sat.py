from ..payload import *
from ..message import *


svs_fields = Fields(
    ("gnssId", U1),
    ("svId", U1),
    ("cno", U1),
    ("elev", I1),
    ("azim", I2),
    ("prRes", I2),
    ("flags", X4),
)

payload_description = Fields(
    ("iTOW", U4),
    ("version", U1),
    ("numSvs", U1),
    ("reserved1", List([U1, U1])),
    ("meas", Loop(key = "numSvs", description = svs_fields))
)

description = MessageDescription(
    name="NAV-SAT",
    message_class=b"\x01",
    message_id=b"\x35",
    payload_description=Options(
        Empty,
        payload_description
    )
)
