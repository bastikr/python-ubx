from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


flags = Bitfield(1, entries=[
    BitfieldEntry("raw", 0),
    BitfieldEntry("difference", 1)
])

payload_description = Fields(
    ("version", U1),
    ("oscId", U1),
    ("flags", flags),
    ("reserved1", U1),
    ("value", I4)
)

description = MessageDescription(
    message_class=TIM,
    message_id=MessageId("HOC", b"\x17"),
    payload_description=Options(
        payload_description
    )
)
