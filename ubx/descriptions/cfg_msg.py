from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("msgClass", U1),
    ("msgID", U1)
)

payload_description1 = Fields(
    ("msgClass", U1),
    ("msgID", U1),
    ("rate", 6*U1)
)

payload_description2 = Fields(
    ("msgClass", U1),
    ("msgID", U1),
    ("rate", U1)
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("MSG", b"\x01"),
    payload_description=Options(
        payload_description0,
        payload_description1,
        payload_description2
    )
)
