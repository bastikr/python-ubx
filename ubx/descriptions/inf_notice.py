from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("str", Chars(None)),
)

description = MessageDescription(
    name="INF-NOTICE",
    message_class=b"\x04",
    message_id=b"\x02",
    payload_description=Options(
        payload_description0,
    )
)
