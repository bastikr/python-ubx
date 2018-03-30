from ..payload import *
from ..message import *

meas_fields = Fields(
    Field("prMes", R8),
    Field("cpMes", R8),
    Field("doMes", R4),
    Field("gnssId", U1),
    Field("svId", U1),
    Field("reserved2", U1),
    Field("freqId", U1),
    Field("locktime", U2),
    Field("cno", U1),
    Field("prStdev", X1),
    Field("doStdev", X1),
    Field("trkStat", X1),
    Field("reserved3", U1)
)

payload_description = Fields(
    Field("rcvTow", R8),
    Field("week", U2),
    Field("leapS", I1),
    Field("numMeas", U1),
    Field("recStat", X1),
    Field("reserved1a", U1),
    Field("reserved1b", U1),
    Field("reserved1c", U1),
    Field("meas", Loop(key = "numMeas", description = meas_fields))
)

description = MessageDescription(
    name = "RXM-RAWX",
    message_class = b"\x02",
    message_id = b"\x15",
    payload_description = payload_description
)

