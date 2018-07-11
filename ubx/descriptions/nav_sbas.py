from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


service = Bitfield(1, entries=[
    BitfieldEntry("Ranging", 0),
    BitfieldEntry("Corrections", 1),
    BitfieldEntry("Integrity", 2),
    BitfieldEntry("Testmode", 3),
])

svs_fields = Fields(
    ("svid", U1),
    ("flags", U1),
    ("udre", U1),
    ("svSys", U1),
    ("svService", U1),
    ("reserved2", U1),
    ("prc", I2),
    ("reserved3", 2*U1),
    ("ic", I2),
)

payload_description = Fields(
    ("iTOW", U4),
    ("geo", U1),
    ("mode", U1),
    ("sys", I1),
    ("service", service),
    ("cnt", U1),
    ("reserved1", 3*U1),
    ("svs", KeyLoop("cnt", svs_fields))
)

description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("SBAS", b"\x32"),
    payload_description=Options(
        Empty,
        payload_description
    )
)
