from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


valid = Bitfield(1, entries=[
    BitfieldEntry("validCurrLs", 0),
    BitfieldEntry("validTimeToLsEvent", 1),
])

payload_description0 = Fields(
    ("iTOW", U4),
    ("version", U1),
    ("reserved1", 3*U1),
    ("srcOfCurrLs", U1),
    ("currLs", I1),
    ("srcOfLsChange", U1),
    ("lsChange", I1),
    ("timeToLsEvent", I4),
    ("dateOfLsGpsWn", U2),
    ("dateOfLsGpsDn", U2),
    ("reserved2", 3*U1),
    ("valid", valid),
)

description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("TIMELS", b"\x26"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
