from ..classid import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("iTOW", U4),
    ("dur", U4),
    ("meanX", I4),
    ("meanY", I4),
    ("meanZ", I4),
    ("meanXHP", I1),
    ("meanYHP", I1),
    ("meanZHP", I1),
    ("reserved2", U1),
    ("meanAcc", U4),
    ("obs", U4),
    ("valid", U1),
    ("active", U1),
    ("reserved3", 2*U1)
)

description = MessageDescription(
    name="NAV-SVIN",
    message_class=NAV,
    message_id=b"\x3b",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
