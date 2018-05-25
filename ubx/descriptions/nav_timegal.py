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
    name="NAV-TIMEGAL",
    message_class=b"\x01",
    message_id=b"\x25",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
