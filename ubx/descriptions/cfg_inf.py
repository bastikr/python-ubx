from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("protocolID", U1),
)

infMsgMask = Bitfield(1, entries=[
    BitfieldEntry("ERROR", 0),
    BitfieldEntry("WARNING", 1),
    BitfieldEntry("NOTICE", 2),
    BitfieldEntry("TEST", 3),
    BitfieldEntry("DEBUG", 4),
])

payload_description1 = MatchedLoop(
    Fields(
        ("protocolID", U1),
        ("reserved1", 3*U1),
        ("infMsgMask", 6*infMsgMask)
    )
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("INF", b"\x02"),
    payload_description=Options(
        payload_description0,
        payload_description1,
    )
)
