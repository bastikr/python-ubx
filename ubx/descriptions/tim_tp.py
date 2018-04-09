from ..payload import *
from ..message import *


payload_description = Fields(
    ("towMS", U4),
    ("towSubMS", U4),
    ("qErr", I4),
    ("week", U2),
    ("flags", X1),
    ("refInfo", X1)
)

description = MessageDescription(
    name = "TIM-TP",
    message_class = b"\x0D",
    message_id = b"\x01",
    payload_description = payload_description
)
