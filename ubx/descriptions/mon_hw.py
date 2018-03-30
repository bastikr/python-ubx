from ..payload import *
from ..message import *

payload_description = Fields(
    Field("pinSel", X4),
    Field("pinBank", X4),
    Field("pinDir", X4),
    Field("pinVal", X4),
    Field("noisePerMS", U2),
    Field("agcCnt", U2),
    Field("aStatus", U1),
    Field("aPower", U1),
    Field("flags", X1),
    Field("reserved1", U1),
    Field("usedMask", X4),
    Field("VP", List(17*[U1])),
    Field("jamInd", U1),
    Field("reserved2", U2),
    Field("pinIrq", X4),
    Field("pullH", X4),
    Field("pullL", X4)
)

description = MessageDescription(
    name = "MON-HW",
    message_class = b"\x0a",
    message_id = b"\x09",
    payload_description = payload_description
)

