from ..classid import *
from ..payload import *
from ..message import *


status = Bitfield(1, entries=[
    BitfieldEntry("recording", 3),
    BitfieldEntry("inactive", 4),
    BitfieldEntry("circular", 5)
])

payload_description = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("filestoreCapacity", U4),
    ("reserved2", 8*U1),
    ("currentMaxLogSize", U4),
    ("currentLogSize", U4),
    ("entryCount", U4),
    ("oldestYear", U2),
    ("oldestMonth", U1),
    ("oldestDay", U1),
    ("oldestHour", U1),
    ("oldestMinute", U1),
    ("oldestSecond", U1),
    ("reserved3", U1),
    ("newestYear", U2),
    ("newestMonth", U1),
    ("newestDay", U1),
    ("newestHour", U1),
    ("newestMinute", U1),
    ("newestSecond", U1),
    ("reserved4", U1),
    ("status", status),
    ("reserved5", 3*U1)
)

description = MessageDescription(
    name="LOG-INFO",
    message_class=LOG,
    message_id=b"\x08",
    payload_description=Options(
        Empty,
        payload_description
    )
)
