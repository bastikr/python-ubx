from ..classid import *
from ..payload import *
from ..message import *


payload_description_eph = Fields(
    ("type", U1),
    ("version", U1),
    ("svId", U1),
    ("reserved1", U1),
    ("FT", U1),
    ("B", U1),
    ("M", U1),
    ("H", I1),
    ("x", I4),
    ("y", I4),
    ("z", I4),
    ("dx", I4),
    ("dy", I4),
    ("dz", I4),
    ("ddx", I1),
    ("ddy", I1),
    ("ddz", I1),
    ("tb", U1),
    ("gamma", I2),
    ("E", U1),
    ("deltaTau", I1),
    ("tau", I4),
    ("reserved2", 4*U1)
)

payload_description_alm = Fields(
    ("type", U1),
    ("version", U1),
    ("svId", U1),
    ("reserved1", U1),
    ("N", U2),
    ("M", U1),
    ("C", U1),
    ("tau", I2),
    ("epsilon", U2),
    ("lambda", I4),
    ("deltaI", I4),
    ("tLambda", U4),
    ("deltaT", I4),
    ("deltaDT", I1),
    ("H", I1),
    ("omega", I2),
    ("reserved2", 4*U1)
)

payload_description_timeoffset = Fields(
    ("type", U1),
    ("version", U1),
    ("N", U2),
    ("tauC", I4),
    ("tauGps", I4),
    ("B1", I2),
    ("B2", I2),
    ("reserved1", 4*U1)
)

description = MessageDescription(
    name="MGA-GLO",
    message_class=MGA,
    message_id=b"\x06",
    payload_description=Options(
        payload_description_eph,
        payload_description_alm,
        payload_description_timeoffset
    )
)
