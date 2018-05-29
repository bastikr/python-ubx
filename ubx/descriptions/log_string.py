from ..classid import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("bytes", MatchedLoop(U1))
)

description = MessageDescription(
    name="LOG-STRING",
    message_class=LOG,
    message_id=b"\x04",
    payload_description=Options(
        payload_description
    )
)
