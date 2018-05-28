from ..classid import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("majA", R8),
    ("flat", R8),
    ("dX", R4),
    ("dY", R4),
    ("dZ", R4),
    ("rotX", R4),
    ("rotY", R4),
    ("rotZ", R4),
    ("scale", R4)
)

payload_description1 = Fields(
    ("datumNum", U2),
    ("datumName", Chars(6)),
    ("majA", R8),
    ("flat", R8),
    ("dX", R4),
    ("dY", R4),
    ("dZ", R4),
    ("rotX", R4),
    ("rotY", R4),
    ("rotZ", R4),
    ("scale", R4)
)

description = MessageDescription(
    name="CFG-DAT",
    message_class=CFG,
    message_id=b"\x06",
    payload_description=Options(
        Empty,
        payload_description0,
        payload_description1,
    )
)
