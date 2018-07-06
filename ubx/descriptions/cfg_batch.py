from ..message_class import *
from ..payload import *
from ..message import *


flags = Bitfield(2, entries=[
    BitfieldEntry("enable", 0),
    BitfieldEntry("extraPvt", 2),
    BitfieldEntry("extraOdo", 3),
    BitfieldEntry("pioEnable", 5),
    BitfieldEntry("pioActiveLow", 6)

])

payload_description0 = Fields(
    ("version", U1),
    ("flags", flags),
    ("bufSize", U2),
    ("notifThrs", U2),
    ("pioId", U1),
    ("reserved1", U1)
)

description = MessageDescription(
    name="CFG-BATCH",
    message_class=CFG,
    message_id=b"\x93",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
