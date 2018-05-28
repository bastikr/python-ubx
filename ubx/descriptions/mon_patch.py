from ..classid import *
from ..payload import *
from ..message import *


patchInfo = Bitfield(4, entries=[
    BitfieldEntry("activated", 0),
    BitfieldEntry("location", slice(1, 3))
])

entry = Fields(
    ("patchInfo", patchInfo),
    ("comparatorNumber", U4),
    ("patchAddress", U4),
    ("patchData", U4)
)

payload_description = Fields(
    ("version", U2),
    ("nEntries", U2),
    ("entries", KeyLoop("nEntries", entry))
)

description = MessageDescription(
    name="MON-PATCH",
    message_class=MON,
    message_id=b"\x27",
    payload_description=Options(
        Empty,
        payload_description
    )
)
