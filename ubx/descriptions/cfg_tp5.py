from ..classid import *
from ..payload import *
from ..message import *


# flags = Bitfield(4, entries=[
#     BitfieldEntry("active", 0),
#     BitfieldEntry("lockGpsFreq", 1),
#     BitfieldEntry("lockedOtherSet", 2),
#     BitfieldEntry("isFreq", 3),
#     BitfieldEntry("isLength", 4),
#     BitfieldEntry("alignToTow", 5),
#     BitfieldEntry("polarity", 6),
#     BitfieldEntry("gridUtcGps", 7),
# ])

flags = Bitfield(4, entries=[
    BitfieldEntry("active", 0),
    BitfieldEntry("lockGpsFreq", 1),
    BitfieldEntry("lockedOtherSet", 2),
    BitfieldEntry("isFreq", 3),
    BitfieldEntry("isLength", 4),
    BitfieldEntry("alignToTow", 5),
    BitfieldEntry("polarity", 6),
    BitfieldEntry("gridUtcGnss", slice(7, 11)),
    BitfieldEntry("syncMode", slice(11, 13)),
])

payload_description0 = Fields(
    ("tpIdx", U1)
)

payload_description1 = Fields(
    ("tpIdx", U1),
    ("version", U1),
    ("reserved1", 2*U1),
    ("antCableDelay", I2),
    ("rfGroupDelay", I2),
    ("freqPeriod", U4),
    ("freqPeriodLock", U4),
    ("pulseLenRation", U4),
    ("pulseLenRationLock", U4),
    ("userConfigDelay", I4),
    ("flags", flags)
)

description = MessageDescription(
    name="CFG-TP5",
    message_class=CFG,
    message_id=b"\x31",
    payload_description=Options(
        Empty,
        payload_description0,
        payload_description1,
    )
)
