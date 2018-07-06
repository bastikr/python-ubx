from ..message_class import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("type", U1)
)

payload_description1 = Fields(
    ("type", U1),
    ("version", U1),
    ("oscId", U1),
    ("srcId", U1),
    ("reserved1", 2*U1),
    ("raw0", U2),
    ("raw1", U2),
    ("maxStepSize", U2)
)

payload_description2 = Fields(
    ("type", U1),
    ("version", U1),
    ("oscId", U1),
    ("reserved1", 3*U1),
    ("gainUncertainty", U2),
    ("gainVco", I4)
)

description = MessageDescription(
    name="TIM-VCOCAL",
    message_class=TIM,
    message_id=b"\x15",
    payload_description=Options(
        Empty,
        payload_description0,
        payload_description1,
        payload_description2
    )
)
