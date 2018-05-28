from ..classid import *
from ..payload import *
from ..message import *


description = MessageDescription(
    name="NAV-RESETODO",
    message_class=NAV,
    message_id=b"\x10",
    payload_description=Options(
        Empty
    )
)
