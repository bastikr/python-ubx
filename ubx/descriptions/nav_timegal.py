from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


valid = Bitfield(1, entries=[
    BitfieldEntry("galTowValid", 0),
    BitfieldEntry("galWnoValid", 1),
    BitfieldEntry("leapSValid", 2),
])

payload_description0 = Fields(
    ("iTOW", U4),
    ("galTow", U4),
    ("fGalTow", I4),
    ("galWno", I2),
    ("leapS", I1),
    ("valid", valid),
    ("tAcc", U4)
)

description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("TIMEGAL", b"\x25"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
