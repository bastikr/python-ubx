from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


globalFlags = Bitfield(1, (
    BitfieldEntry("chipGen", slice(0, 3)),
    )
)

flags = Bitfield(1, (
    BitfieldEntry("svUsed", 0),
    BitfieldEntry("diffCorr", 1),
    BitfieldEntry("orbitAvail", 2),
    BitfieldEntry("orbitEph", 3),
    BitfieldEntry("unhealthy", 4),
    BitfieldEntry("orbitAlm", 5),
    BitfieldEntry("orbitAop", 6),
    BitfieldEntry("smoothed", 7),
    )
)

quality = Bitfield(1, (
    BitfieldEntry("qualityInd", slice(0, 4)),
    )
)

chn_fields = Fields(
  ("chn", U1),
  ("svid", U1),
  ("flags", flags),
  ("quality", quality),
  ("cno", U1),
  ("elev", I1),
  ("azim", I2),
  ("prRes", I4)
)

payload_description0 = Fields(
    ("iTOW", U4),
    ("numCh", U1),
    ("globalFlags", globalFlags),
    ("reserved1", 2*U1),
    ("ch", KeyLoop("numCh", chn_fields)),
)

description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("SVINFO", b"\x30"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
