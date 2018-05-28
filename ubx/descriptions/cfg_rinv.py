from ..classid import *
from ..payload import *
from ..message import *

flags = Bitfield(1, entries=[
    BitfieldEntry("dump", 0),
    BitfieldEntry("binary", 1),
])

payload_description0 = Fields(
    ("flags", flags),
    ("data", MatchedLoop(U1))
)

description = MessageDescription(
    name="CFG-RINV",
    message_class=CFG,
    message_id=b"\x34",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
