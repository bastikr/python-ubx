from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


valid = Bitfield(1, entries=[
    BitfieldEntry("validDate", 0),
    BitfieldEntry("validTime", 1),
    BitfieldEntry("fullyResolved", 2)
])

flags = Bitfield(1, entries=[
    BitfieldEntry("GPSfixOK", 0),
    BitfieldEntry("DiffSoln", 1),
    BitfieldEntry("WKNSET", 2),
    BitfieldEntry("TOWSET", 3),
    BitfieldEntry("headVehValid", 4)
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
    ("nano", I4),
    ("gpsFix", U1),
    ("flags", flags),
    ("reserved1", 2*U1),
    ("lon", I4),
    ("lat", I4),
    ("height", I4),
    ("hMSL", I4),
    ("gSpeed", I4),
    ("speed", I4),
    ("headMot", I4),
    ("headVeh", I4),
    ("hAcc", U4),
    ("vAcc", U4),
    ("sAcc", U4),
    ("headAcc", U4),
    ("reserved2", 4*U1)
)

description = MessageDescription(
    message_class=HNR,
    message_id=MessageId("PVT", b"\x00"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
