from ..payload import *
from ..message import *


flags = Bitfield(1, (
    BitfieldEntry("rtcCalib", 0),
    BitfieldEntry("safeBoot", 1),
    BitfieldEntry("jammingState", slice(2, 4)),
    BitfieldEntry("xtalAbsent", 4),
    )
)

payload_description = Fields(
    ("pinSel", X4),
    ("pinBank", X4),
    ("pinDir", X4),
    ("pinVal", X4),
    ("noisePerMS", U2),
    ("agcCnt", U2),
    ("aStatus", U1),
    ("aPower", U1),
    ("flags", flags),
    ("reserved1", U1),
    ("usedMask", X4),
    ("VP", 17*U1),
    ("jamInd", U1),
    ("reserved2", U2),
    ("pinIrq", X4),
    ("pullH", X4),
    ("pullL", X4)
)

description = MessageDescription(
    name="MON-HW",
    message_class=b"\x0a",
    message_id=b"\x09",
    payload_description=Options(
        Empty,
        payload_description
    )
)
