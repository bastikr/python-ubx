from ..classid import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("pending", 6*U2),
    ("usage", 6*U1),
    ("peakUsage", 6*U1)
)

description = MessageDescription(
    name="MON-RXBUF",
    message_class=MON,
    message_id=b"\x07",
    payload_description=Options(
        Empty,
        payload_description
    )
)
