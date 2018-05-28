from ..classid import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("str", Chars(None)),
)

description = MessageDescription(
    name="INF-WARNING",
    message_class=INF,
    message_id=b"\x01",
    payload_description=Options(
        payload_description0,
    )
)
