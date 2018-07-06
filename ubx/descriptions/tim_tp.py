from ..message_class import *
from ..payload import *
from ..message import *


flags = Bitfield(1, (
    BitfieldEntry("timeBase", 0),
    BitfieldEntry("utc", 1),
    BitfieldEntry("raim", slice(2, 4)),
    )
)

refInfo = Bitfield(1, (
    BitfieldEntry("timeRefGnss", slice(0, 4)),
    BitfieldEntry("utcStandard", slice(4, 8)),
    )
)

payload_description = Fields(
    ("towMS", U4),
    ("towSubMS", U4),
    ("qErr", I4),
    ("week", U2),
    ("flags", flags),
    ("refInfo", refInfo)
)

description = MessageDescription(
    name="TIM-TP",
    message_class=TIM,
    message_id=b"\x01",
    payload_description=Options(
        Empty,
        payload_description
    )
)
