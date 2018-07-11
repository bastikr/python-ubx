from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description_data = Fields(
    ("type", U1),
    ("version", U1),
    ("sequence", U2),
    ("size", U2),
    ("data", KeyLoop("size", U1))
)

payload_description_stop = Fields(
    ("type", U1),
    ("version", U1)
)

payload_description_ack = Fields(
    ("type", U1),
    ("version", U1),
    ("ack", U1),
    ("reserved1", U1),
    ("sequence", U2)
)

description = MessageDescription(
    message_class=MGA,
    message_id=MessageId("FLASH", b"\x21"),
    payload_description=Options(
        payload_description_stop,
        payload_description_ack,
        payload_description_data
    )
)
