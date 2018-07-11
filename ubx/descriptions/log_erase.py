from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


description = MessageDescription(
    message_class=LOG,
    message_id=MessageId("ERASE", b"\x03"),
    payload_description=Options(
        Empty
    )
)
