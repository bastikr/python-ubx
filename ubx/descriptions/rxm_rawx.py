from ..classid import *
from ..payload import *
from ..message import *


recStat = Bitfield(1, (
    BitfieldEntry("leapSec", 0),
    BitfieldEntry("clkReset", 1),
    )
)

prStdev = Bitfield(1, (
    BitfieldEntry("prStd", slice(0, 4)),
    )
)

cpStdev = Bitfield(1, (
    BitfieldEntry("cpStd", slice(0, 4)),
    )
)

doStdev = Bitfield(1, (
    BitfieldEntry("doStd", slice(0, 4)),
    )
)

trkStat = Bitfield(1, (
    BitfieldEntry("prValid", 0),
    BitfieldEntry("cpValid", 1),
    BitfieldEntry("halfCyc", 2),
    BitfieldEntry("subHalfCyc", 3),
    )
)

meas_fields = Fields(
    ("prMes", R8),
    ("cpMes", R8),
    ("doMes", R4),
    ("gnssId", U1),
    ("svId", U1),
    ("reserved2", U1),
    ("freqId", U1),
    ("locktime", U2),
    ("cno", U1),
    ("prStdev", prStdev),
    ("cpStdev", cpStdev),
    ("doStdev", doStdev),
    ("trkStat", trkStat),
    ("reserved3", U1)
)

payload_description = Fields(
    ("rcvTow", R8),
    ("week", U2),
    ("leapS", I1),
    ("numMeas", U1),
    ("recStat", recStat),
    ("version", U1),
    ("reserved1", 2*U1),
    ("meas", KeyLoop("numMeas", meas_fields))
)

description = MessageDescription(
    name="RXM-RAWX",
    message_class=RXM,
    message_id=b"\x15",
    payload_description=Options(
        Empty,
        payload_description,
    )
)
