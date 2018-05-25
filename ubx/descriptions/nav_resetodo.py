from ..payload import *
from ..message import *


description = MessageDescription(
    name="NAV-RESETODO",
    message_class=b"\x01",
    message_id=b"\x10",
    payload_description=Options(
        Empty
    )
)
