from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


flags = Bitfield(1, entries=[
    BitfieldEntry("src", slice(0, 3)),
])

payload_description = Fields(
    ("itow", I4),
    ("frac", I4),
    ("deltaMs", I4),
    ("deltaNs", I4),
    ("wno", U2),
    ("flags", flags),
    ("reserved1", U1)
)

description = MessageDescription(
    message_class=TIM,
    message_id=MessageId("VRFY", b"\x06"),
    payload_description=Options(
        Empty,
        payload_description
    )
)
