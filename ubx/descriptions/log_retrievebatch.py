from ..classid import *
from ..payload import *
from ..message import *


flags = Bitfield(1, entries=[
    BitfieldEntry("sendMonFirst", 0)
])

payload_description = Fields(
    ("version", U1),
    ("flags", flags),
    ("reserved1", 2*U1)
)

description = MessageDescription(
    name="LOG-RETRIEVEBATCH",
    message_class=LOG,
    message_id=b"\x10",
    payload_description=Options(
        payload_description
    )
)
