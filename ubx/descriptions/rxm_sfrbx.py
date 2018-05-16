from ..payload import *
from ..message import *


words_fields = Fields(
    ("dwrd", U4)
)

payload_description = Fields(
    ("gnssId", U1),
    ("svId", U1),
    ("reserved1", U1),
    ("freqId", U1),
    ("numWords", U1),
    ("chn", U1),
    ("version", U1),
    ("reserved2", U1),
    ("meas", KeyLoop(key="numWords", description=words_fields))
)

description = MessageDescription(
    name="RXM-SFRBX",
    message_class=b"\x02",
    message_id=b"\x13",
    payload_description=Options(
        Empty,
        payload_description
    )
)
