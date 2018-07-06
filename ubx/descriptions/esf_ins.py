from ..message_class import *
from ..payload import *
from ..message import *


bitfield0 = Bitfield(4, entries=[
    BitfieldEntry("version", slice(0, 8)),
    BitfieldEntry("xAngRateValid", 8),
    BitfieldEntry("yAngRateValid", 9),
    BitfieldEntry("zAngRateValid", 10),
    BitfieldEntry("xAccelValid", 11),
    BitfieldEntry("yAccelValid", 12),
    BitfieldEntry("zAccelValid", 13),
])

payload_description0 = Fields(
    ("bitfield0", bitfield0),
    ("reserved1", 4*U1),
    ("iTOW", U4),
    ("xAngRate", I4),
    ("yAngRate", I4),
    ("zAngRate", I4),
    ("xAccel", I4),
    ("yAccel", I4),
    ("zAccel", I4),
)

description = MessageDescription(
    name="ESF-INS",
    message_class=ESF,
    message_id=b"\x15",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
