from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("str", Chars(None)),
)

description = MessageDescription(
    name="INF-TEST",
    message_class=b"\x04",
    message_id=b"\x03",
    payload_description=Options(
        payload_description0,
    )
)
