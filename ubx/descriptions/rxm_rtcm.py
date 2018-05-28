from ..payload import *
from ..message import *


flags = Bitfield(1, entries=[
    BitfieldEntry("crcFailed", 0)
])

payload_description0 = Fields(
    ("version", U1),
    ("flags", flags),
    ("reserved1", 2*U1),
    ("refStation", U2),
    ("msgType", U2)
)

description = MessageDescription(
    name="RXM-RTCM",
    message_class=b"\x02",
    message_id=b"\x32",
    payload_description=Options(
        payload_description0
    )
)