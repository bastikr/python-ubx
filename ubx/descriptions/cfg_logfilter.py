from ..classid import *
from ..payload import *
from ..message import *


flags = Bitfield(1, entries=[
    BitfieldEntry("recordEnabled", 0),
    BitfieldEntry("psmOncePerWakupEnabled", 1),
    BitfieldEntry("applyAllFilterSettings", 2),
])

payload_description0 = Fields(
    ("version", U1),
    ("flags", flags),
    ("minInterval", U2),
    ("timeThreshold", U2),
    ("speedThreshold", U2),
    ("positionThreshold", U4),
)

description = MessageDescription(
    name="CFG-LOGFILTER",
    message_class=CFG,
    message_id=b"\x47",
    payload_description=Options(
        Empty,
        payload_description0
    )
)
