from ..payload import *
from ..message import *


flags = Bitfield(4, entries=[
    BitfieldEntry("gnssFixOK", 0),
    BitfieldEntry("diffSoln", 1),
    BitfieldEntry("relPosValid", 2),
    BitfieldEntry("carrSoln", slice(3, 5)),
    BitfieldEntry("isMoving", 5),
    BitfieldEntry("refPosMiss", 6),
    BitfieldEntry("refObsMiss", 7)
])

payload_description0 = Fields(
    ("version", U1),
    ("reserved1", U1),
    ("refStationId", U2),
    ("iTOW", U4),
    ("relPosN", I4),
    ("relPosE", I4),
    ("relPosD", I4),
    ("relPosHPN", I1),
    ("relPosHPE", I1),
    ("relPosHPD", I1),
    ("reserved2", U1),
    ("accN", U4),
    ("accE", U4),
    ("accD", U4),
    ("flags", flags)
)

description = MessageDescription(
    name="NAV-RELPOSNED",
    message_class=b"\x01",
    message_id=b"\x3c",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
