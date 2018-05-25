from ..payload import *
from ..message import *


svFlag = Bitfield(1, entries=[
    BitfieldEntry("health", slice(0, 2)),
    BitfieldEntry("visibility", slice(2, 4))
])

eph = Bitfield(1, entries=[
    BitfieldEntry("ephUsability", slice(0, 5)),
    BitfieldEntry("ephSource", slice(5, 8))
])

alm = Bitfield(1, entries=[
    BitfieldEntry("almUsability", slice(0, 5)),
    BitfieldEntry("almSource", slice(5, 8))
])

otherOrb = Bitfield(1, entries=[
    BitfieldEntry("anoAopUsability", slice(0, 5)),
    BitfieldEntry("type", slice(5, 8))
])

sv = Fields(
    ("gnssId", U1),
    ("svId", U1),
    ("svFlag", svFlag),
    ("eph", eph),
    ("alm", alm),
    ("otherOrb", otherOrb)
)

payload_description0 = Fields(
    ("iTOW", U4),
    ("version", U1),
    ("numSv", U1),
    ("reserved1", 2*U1),
    ("svs", KeyLoop("numSv", sv))
)

description = MessageDescription(
    name="NAV-ORB",
    message_class=b"\x01",
    message_id=b"\x34",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
