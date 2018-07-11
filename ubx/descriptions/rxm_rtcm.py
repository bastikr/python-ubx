from ..message_class import *
from ..message_id import *
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
    message_class=RXM,
    message_id=MessageId("RTCM", b"\x32"),
    payload_description=Options(
        payload_description0
    )
)
