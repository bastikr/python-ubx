from ..message_class import *
from ..payload import *
from ..message import *


aopCfg = Bitfield(1, entries=[
    BitfieldEntry("useAOP", 0)
])

payload_description0 = Fields(
    ("iTOW", U4),
    ("aopCfg", aopCfg),
    ("status", U1),
    ("reserved1", 10*U1)
)

description = MessageDescription(
    name="NAV-AOPSTATUS",
    message_class=NAV,
    message_id=b"\x60",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
