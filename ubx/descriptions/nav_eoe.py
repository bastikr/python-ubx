from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("iTOW", U4),
)

description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("EOE", b"\x61"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
