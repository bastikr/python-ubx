from ..classid import *
from ..payload import *
from ..message import *


flags = Bitfield(1, [
    BitfieldEntry("towSet", slice(0, 2))
])

sv = Fields(
    ("gnssId", U1),
    ("svId", U1),
    ("cNo", U1),
    ("mpathIndic", U1),
    ("dopplerMS", I4),
    ("dopplerHz", I4),
    ("wholeChips", U2),
    ("fracChips", U2),
    ("codePhase", U4),
    ("intCodePhase", U1),
    ("pseuRangeRMSErr", U1),
    ("reserved5", 2*U1)
)

payload_description0 = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("gpsTOW", U4),
    ("gloTOW", U4),
    ("bdsTOW", U4),
    ("reserved2", 4*U1),
    ("qzssTOW", U4),
    ("gpsTOWacc", U2),
    ("gloTOWacc", U2),
    ("bdsTOWacc", U2),
    ("reserved3", 2*U1),
    ("qzssTOWacc", U2),
    ("numSV", U1),
    ("flags", flags),
    ("reserved4", 8*U1),
    ("svs", KeyLoop("numSV", sv))
)

description = MessageDescription(
    name="RXM-MEASX",
    message_class=RXM,
    message_id=b"\x14",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
