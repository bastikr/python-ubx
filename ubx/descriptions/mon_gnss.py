from ..classid import *
from ..payload import *
from ..message import *


supported = Bitfield(1, entries=[
    BitfieldEntry("GPSSup", 0),
    BitfieldEntry("GlonassSup", 1),
    BitfieldEntry("BeidouSup", 2),
    BitfieldEntry("GalileoSup", 3)
])

defaultGnss = Bitfield(1, entries=[
    BitfieldEntry("GPSDef", 0),
    BitfieldEntry("GlonassDef", 1),
    BitfieldEntry("BeidouDef", 2),
    BitfieldEntry("GalileoDef", 3)
])

enabled = Bitfield(1, entries=[
    BitfieldEntry("GPSEna", 0),
    BitfieldEntry("GlonassEna", 1),
    BitfieldEntry("BeidouEna", 2),
    BitfieldEntry("GalileoEna", 3)
])

payload_description = Fields(
    ("version", U1),
    ("supported", supported),
    ("defaultGnss", defaultGnss),
    ("enabled", enabled),
    ("simultaneous", U1),
    ("reserved1", 3*U1),
)

description = MessageDescription(
    name="MON-GNSS",
    message_class=MON,
    message_id=b"\x28",
    payload_description=Options(
        Empty,
        payload_description
    )
)
