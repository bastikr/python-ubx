from ..classid import *
from ..payload import *
from ..message import *


valid = Bitfield(1, entries=[
    BitfieldEntry("validDate", 0),
    BitfieldEntry("validTime", 1),
    BitfieldEntry("fullyResolved", 2),
    BitfieldEntry("validMag", 3),
])

flags = Bitfield(1, entries=[
    BitfieldEntry("gnssFixOK", 0),
    BitfieldEntry("diffSoln", 1),
    BitfieldEntry("psmState", slice(2, 5)),
    BitfieldEntry("headVehValid", 5),
    BitfieldEntry("carrSoln", slice(6, 8)),
])

flags2 = Bitfield(1, entries=[
    BitfieldEntry("confirmedAvai", 5),
    BitfieldEntry("confirmedDate", 6),
    BitfieldEntry("confirmedTime", 7),
])

payload_description0 = Fields(
    ("iTOW", U4),
    ("year", U2),
    ("month", U1),
    ("day", U1),
    ("hour", U1),
    ("min", U1),
    ("sec", U1),
    ("valid", valid),
    ("tAcc", U4),
    ("nano", I4),
    ("fixType", U1),
    ("flags", flags),
    ("flags2", flags2),
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
    ("reserved1", 6*U1),
    ("headVeh", I4),
    ("magDec", I2),
    ("magAcc", U2)
)

description = MessageDescription(
    name="NAV-PVT",
    message_class=NAV,
    message_id=b"\x07",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
