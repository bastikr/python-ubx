from ..classid import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("iTOW", U4),
    ("intDeltaFreq", I4),
    ("intDeltaFreqUnc", U4),
    ("intRaw", U4),
    ("extDeltaFreq", I4),
    ("extDeltaFreqUnc", U4),
    ("extRaw", U4)
)

description = MessageDescription(
    name="TIM-FCHG",
    message_class=TIM,
    message_id=b"\x16",
    payload_description=Options(
        Empty,
        payload_description
    )
)
