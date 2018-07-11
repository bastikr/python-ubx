from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


flags = Bitfield(1, entries=[
    BitfieldEntry("mode", 0),
    BitfieldEntry("run", 1),
    BitfieldEntry("newFallingEdge", 2),
    BitfieldEntry("timeBase", slice(3, 5)),
    BitfieldEntry("utc", 5),
    BitfieldEntry("time", 6),
    BitfieldEntry("newRisingEdge", 7)
])

payload_description = Fields(
    ("ch", U1),
    ("flags", flags),
    ("count", U2),
    ("wnR", U2),
    ("wnF", U2),
    ("towMsR", U4),
    ("towSubMsR", U4),
    ("towMsF", U4),
    ("towSubMsF", U4),
    ("accEst", U4)
)

description = MessageDescription(
    message_class=TIM,
    message_id=MessageId("TM2", b"\x03"),
    payload_description=Options(
        Empty,
        payload_description
    )
)
