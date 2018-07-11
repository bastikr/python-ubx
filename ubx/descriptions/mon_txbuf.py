from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


errors = Bitfield(1, entries=[
    BitfieldEntry("limit", slice(0, 6)),
    BitfieldEntry("mem", 6),
    BitfieldEntry("alloc", 7)
])

payload_description = Fields(
    ("pending", 6*U2),
    ("usage", 6*U1),
    ("peakUsage", 6*U1),
    ("tUsage", U1),
    ("tPeakusage", U1),
    ("errors", errors),
    ("reserved1", U1)
)

description = MessageDescription(
    message_class=MON,
    message_id=MessageId("TXBUF", b"\x08"),
    payload_description=Options(
        Empty,
        payload_description
    )
)
