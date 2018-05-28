from ..classid import *
from ..payload import *
from ..message import *


mode = Bitfield(1, entries=[
    BitfieldEntry("enabled", 0),
    BitfieldEntry("test", 1)
])

usage = Bitfield(1, entries=[
    BitfieldEntry("range", 0),
    BitfieldEntry("diffCor", 1),
    BitfieldEntry("integrity", 2)
])

scanmode2 = Bitfield(1, entries=[
    BitfieldEntry("PRN152", 0),
    BitfieldEntry("PRN153", 1),
    BitfieldEntry("PRN154", 3),
    BitfieldEntry("PRN155", 4),
    BitfieldEntry("PRN156", 5),
    BitfieldEntry("PRN157", 6),
    BitfieldEntry("PRN158", 7),
])

scanmode1 = Bitfield(4, entries=[
    BitfieldEntry("PRN120", 0),
    BitfieldEntry("PRN121", 1),
    BitfieldEntry("PRN123", 3),
    BitfieldEntry("PRN124", 4),
    BitfieldEntry("PRN125", 5),
    BitfieldEntry("PRN126", 6),
    BitfieldEntry("PRN127", 7),
    BitfieldEntry("PRN128", 8),
    BitfieldEntry("PRN129", 9),
    BitfieldEntry("PRN130", 10),
    BitfieldEntry("PRN131", 11),
    BitfieldEntry("PRN133", 13),
    BitfieldEntry("PRN134", 14),
    BitfieldEntry("PRN135", 15),
    BitfieldEntry("PRN136", 16),
    BitfieldEntry("PRN137", 17),
    BitfieldEntry("PRN138", 18),
    BitfieldEntry("PRN139", 19),
    BitfieldEntry("PRN140", 20),
    BitfieldEntry("PRN141", 21),
    BitfieldEntry("PRN143", 23),
    BitfieldEntry("PRN144", 24),
    BitfieldEntry("PRN145", 25),
    BitfieldEntry("PRN146", 26),
    BitfieldEntry("PRN147", 27),
    BitfieldEntry("PRN148", 28),
    BitfieldEntry("PRN149", 29),
    BitfieldEntry("PRN150", 30),
    BitfieldEntry("PRN151", 31),
])

payload_description0 = Fields(
    ("mode", mode),
    ("usage", usage),
    ("maxSBAS", U1),
    ("scanmode2", scanmode2),
    ("scanmode1", scanmode1),
)

description = MessageDescription(
    name="CFG-SBAS",
    message_class=CFG,
    message_id=b"\x16",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
