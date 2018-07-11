from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("RESETODO", b"\x10"),
    payload_description=Options(
        Empty
    )
)
