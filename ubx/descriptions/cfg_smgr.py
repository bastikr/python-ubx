from ..payload import *
from ..message import *


messageCfg = Bitfield(2, entries=[
    BitfieldEntry("measInternal", 0),
    BitfieldEntry("measGNSS", 1),
    BitfieldEntry("measEXTINT0", 2),
    BitfieldEntry("measEXTINT1", 3),
])

flags = Bitfield(2, entries=[
    BitfieldEntry("disableInternal", 0),
    BitfieldEntry("disableExternal", 1),
    BitfieldEntry("preferenceMode", 2),
    BitfieldEntry("enableGNSS", 3),
    BitfieldEntry("enableEXTINT0", 4),
    BitfieldEntry("enableEXTINT1", 5),
    BitfieldEntry("enableHostMeasInt", 6),
    BitfieldEntry("enableHostMeasExt", 7),
    BitfieldEntry("useAnyFix", 10),
    BitfieldEntry("disableMaxSlewRate", 11),
    BitfieldEntry("issueFreqWarning", 12),
    BitfieldEntry("issueTimeWarning", 13),
    BitfieldEntry("TPCoherent", slice(14, 16)),
    BitfieldEntry("disableOffset", 16),

])

payload_description0 = Fields(
    ("version", U1),
    ("miGNSSFix", U1),
    ("maxFreqChangeRate", U2),
    ("maxPhaseCorrRate", U2),
    ("reserved1", List(2*[U1])),
    ("freqTolerance", U2),
    ("timeTolerance", U2),
    ("messageCfg", messageCfg),
    ("maxSlewRate", U2),
    ("flags", flags)
)

description = MessageDescription(
    name="CFG-SMGR",
    message_class=b"\x06",
    message_id=b"\x62",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
