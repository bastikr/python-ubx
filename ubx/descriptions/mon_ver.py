from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


errors = Bitfield(1, entries=[
    BitfieldEntry("limit", slice(0, 6)),
    BitfieldEntry("mem", 6),
    BitfieldEntry("alloc", 7)
])

payload_description = Fields(
    ("swVersion", Chars(30)),
    ("hwVersion", Chars(10)),
    ("extension", MatchedLoop(Chars(30)))
)

description = MessageDescription(
    message_class=MON,
    message_id=MessageId("VER", b"\x04"),
    payload_description=Options(
        Empty,
        payload_description
    )
)
