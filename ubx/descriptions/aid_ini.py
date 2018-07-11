from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


tmCfg = Bitfield(2, [
    BitfieldEntry("fEdge", 1),
    BitfieldEntry("tm1", 4),
    BitfieldEntry("f1", 6)
])

flags = Bitfield(4, [
    BitfieldEntry("pos", 0),
    BitfieldEntry("time", 1),
    BitfieldEntry("clockD", 2),
    BitfieldEntry("tp", 3),
    BitfieldEntry("clockF", 4),
    BitfieldEntry("lla", 5),
    BitfieldEntry("altInv", 6),
    BitfieldEntry("prevTm", 7),
    BitfieldEntry("utc", 10),
])

payload_description0 = Fields(
    ("ecefXOrLat", I4),
    ("ecefYOrLon", I4),
    ("ecefZOrAlt", I4),
    ("posAcc", U4),
    ("tmCfg", tmCfg),
    ("wnoOrDate", U2),
    ("towOrTime", U4),
    ("towNs", I4),
    ("tAccMs", U4),
    ("tAccNs", U4),
    ("clkDOrFreq", I4),
    ("clkDAccOrFreqAcc", U4),
    ("flags", flags)
)


description = MessageDescription(
    message_class=AID,
    message_id=MessageId("INI", b"\x01"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
