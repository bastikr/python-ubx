from ..message_class import *
from ..payload import *
from ..message import *


flags = Bitfield(4, entries=[
    BitfieldEntry("healthValid", 0),
    BitfieldEntry("utcValid", 1),
    BitfieldEntry("klobValid", 2)
])

payload_description0 = Fields(
    ("health", X4),
    ("utcA0", R8),
    ("utcA1", R8),
    ("utcTOW", I4),
    ("utcWNT", I2),
    ("utcLS", I2),
    ("utcWNF", I2),
    ("utcDN", I2),
    ("utcLSF", I2),
    ("utcSpare", I2),
    ("klobA0", R4),
    ("klobA1", R4),
    ("klobA2", R4),
    ("klobA3", R4),
    ("klobB0", R4),
    ("klobB1", R4),
    ("klobB2", R4),
    ("klobB3", R4),
    ("flags", flags)
)

description = MessageDescription(
    name="AID-HUI",
    message_class=AID,
    message_id=b"\x02",
    payload_description=Options(
        Empty,
        payload_description0
    )
)
