from ..payload import *
from ..message import *

meas_fields = Fields((
    ("prMes", R8),
    ("cpMes", R8),
    ("doMes", R4),
    ("gnssId", U1),
    ("svId", U1),
    ("reserved2", U1),
    ("freqId", U1),
    ("locktime", U2),
    ("cno", U1),
    ("prStdev", X1),
    ("doStdev", X1),
    ("trkStat", X1),
    ("reserved3", U1)
))

payload_description = Fields((
    ("rcvTow", R8),
    ("week", U2),
    ("leapS", I1),
    ("numMeas", U1),
    ("recStat", X1),
    ("reserved1a", U1),
    ("reserved1b", U1),
    ("reserved1c", U1),
    ("meas", Loop(key = "numMeas", description = meas_fields))
))

description = MessageDescription(
    name = "RXM-RAWX",
    message_class = b"\x02",
    message_id = b"\x15",
    payload_description = payload_description
)

