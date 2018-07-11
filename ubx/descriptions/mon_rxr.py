from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


flags = Bitfield(1, entries=[
    BitfieldEntry("awake", 0)
])

payload_description = Fields(
    ("flags", flags),
)

description = MessageDescription(
    message_class=MON,
    message_id=MessageId("RXR", b"\x21"),
    payload_description=Options(
        Empty,
        payload_description
    )
)
