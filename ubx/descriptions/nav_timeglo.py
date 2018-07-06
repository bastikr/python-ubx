from ..message_class import *
from ..payload import *
from ..message import *


valid = Bitfield(1, entries=[
    BitfieldEntry("todValid", 0),
    BitfieldEntry("dateValid", 1),
])

payload_description0 = Fields(
    ("iTOW", U4),
    ("TOD", U4),
    ("fTOD", I4),
    ("Nt", U2),
    ("N4", U1),
    ("valid", valid),
    ("tAcc", U4)
)

description = MessageDescription(
    name="NAV-TIMEGLO",
    message_class=NAV,
    message_id=b"\x23",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
