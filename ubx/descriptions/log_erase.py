from ..classid import *
from ..payload import *
from ..message import *


description = MessageDescription(
    name="LOG-ERASE",
    message_class=LOG,
    message_id=b"\x03",
    payload_description=Options(
        Empty
    )
)
