from ..message_class import *
from ..payload import *
from ..message import *


mask = Bitfield(2, entries=[
    BitfieldEntry("dyn", 0),
    BitfieldEntry("minEl", 1),
    BitfieldEntry("posFixMode", 2),
    BitfieldEntry("drLim", 3),
    BitfieldEntry("posMask", 4),
    BitfieldEntry("timeMask", 5),
    BitfieldEntry("staticHoldMask", 6),
    BitfieldEntry("dgpsMask", 7),
    BitfieldEntry("cnoThreshold", 8),
    BitfieldEntry("utc", 10),
])

payload_description0 = Fields(
    ("mask", mask),
    ("dynModel", U1),
    ("fixMode", U1),
    ("fixedAlt", I4),
    ("fixedAltVar", U4),
    ("minElev", I1),
    ("drLimit", U1),
    ("pDop", U2),
    ("tDop", U2),
    ("pAcc", U2),
    ("tAcc", U2),
    ("staticHoldThresh", U1),
    ("dgnssTimeout", U1),
    ("cnoThreshNumSVs", U1),
    ("cnoThresh", U1),
    ("reserved1", 2*U1),
    ("staticHoldMaxDist", U2),
    ("utcStandard", U1),
    ("reserved2", 5*U1)
)

description = MessageDescription(
    name="CFG-NAV5",
    message_class=CFG,
    message_id=b"\x24",
    payload_description=Options(
        Empty,
        payload_description0
    )
)
