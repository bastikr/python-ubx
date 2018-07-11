from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


flags = Bitfield(1, (
    BitfieldEntry("gpsFixOk", 0),
    BitfieldEntry("diffSoln", 1),
    BitfieldEntry("wknSet", 2),
    BitfieldEntry("towSet", 3),
    BitfieldEntry("reserved", slice(4, 8))
    )
)

fixStat = Bitfield(1, (
    BitfieldEntry("diffCor", 0),
    BitfieldEntry("mapMatching", slice(6, 8))
    )
)

flags2 = Bitfield(1, (
    BitfieldEntry("psmState", slice(0, 2)),
    BitfieldEntry("spoofDetState", slice(3, 5)),
    )
)

payload_description0 = Fields(
    ("iTOW", U4),
    ("gpsFix", U1),
    ("flags", flags),
    ("fixStat", fixStat),
    ("flags2", flags2),
    ("ttff", U4),
    ("msss", U4),
)

description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("STATUS", b"\x03"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
