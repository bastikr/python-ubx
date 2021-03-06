from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("str", Chars(None)),
)

description = MessageDescription(
    message_class=INF,
    message_id=MessageId("WARNING", b"\x01"),
    payload_description=Options(
        payload_description0,
    )
)
