from ..message_class import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("dur", U4),
    ("meanX", I4),
    ("meanY", I4),
    ("meanZ", I4),
    ("meanV", I4),
    ("obs", U4),
    ("valid", U1),
    ("active", U1),
    ("reserved1", 2*U1)
)

description = MessageDescription(
    name="TIM-SVIN",
    message_class=TIM,
    message_id=b"\x04",
    payload_description=Options(
        Empty,
        payload_description
    )
)
