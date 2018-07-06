from ..message_class import *
from ..payload import *
from ..message import *


contentValid = Bitfield(1, entries=[
    BitfieldEntry("extraPvt", 0),
    BitfieldEntry("extraOdo", 1)
])

valid = Bitfield(1, entries=[
    BitfieldEntry("validDate", 0),
    BitfieldEntry("validTime", 1)
])

flags = Bitfield(1, entries=[
    BitfieldEntry("gnssFixOK", 0),
    BitfieldEntry("diffSoln", 1),
    BitfieldEntry("psmState", slice(2, 5)),
])

payload_description = Fields(
    ("version", U1),
    ("contentValid", contentValid),
    ("msgCnt", U2),
    ("iTOW", U4),
    ("year", U2),
    ("month", U1),
    ("day", U1),
    ("hour", U1),
    ("min", U1),
    ("sec", U1),
    ("valid", valid),
    ("tAcc", U4),
    ("fracSec", I4),
    ("fixType", U1),
    ("flags", flags),
    ("flags2", X1),
    ("numSV", U1),
    ("lon", I4),
    ("lat", I4),
    ("height", I4),
    ("hMSL", I4),
    ("hAcc", U4),
    ("vAcc", U4),
    ("velN", I4),
    ("velE", I4),
    ("velD", I4),
    ("gSpeed", I4),
    ("headMot", I4),
    ("sAcc", U4),
    ("headAcc", U4),
    ("pDOP", U2),
    ("reserved1", 2*U1),
    ("distance", U4),
    ("totalDistance", U4),
    ("distanceStd", U4),
    ("reserved2", 4*U1)
)

description = MessageDescription(
    name="LOG-BATCH",
    message_class=LOG,
    message_id=b"\x11",
    payload_description=Options(
        Empty,
        payload_description
    )
)
