from ..classid import *
from ..payload import *
from ..message import *


flags = Bitfield(1, entries=[
    BitfieldEntry("awake", 0)
])

payload_description = Fields(
    ("flags", flags),
)

description = MessageDescription(
    name="MON-RXR",
    message_class=MON,
    message_id=b"\x21",
    payload_description=Options(
        Empty,
        payload_description
    )
)
