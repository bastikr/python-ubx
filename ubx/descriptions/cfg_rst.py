from ..payload import *
from ..message import *


navBbrMask = Bitfield(1, entries=[
    BitfieldEntry("eph", 0),
    BitfieldEntry("alm", 1),
    BitfieldEntry("health", 2),
    BitfieldEntry("klob", 3),
    BitfieldEntry("pos", 4),
    BitfieldEntry("clkd", 5),
    BitfieldEntry("osc", 6),
    BitfieldEntry("utc", 7),
    BitfieldEntry("rtc", 8),
    BitfieldEntry("aop", 15),
])

payload_description0 = Fields(
    ("navBbrMask", navBbrMask),
    ("resetMode", U1)
)

description = MessageDescription(
    name="CFG-RST",
    message_class=b"\x06",
    message_id=b"\x04",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
