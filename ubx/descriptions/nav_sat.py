from ..payload import *
from ..message import *


flags = Bitfield(4, (
    BitfieldEntry("qualityInd", slice(0, 3)),
    BitfieldEntry("svUsed", 3),
    BitfieldEntry("health", slice(4, 6)),
    BitfieldEntry("diffCor", 6),
    BitfieldEntry("smoothed", 7),
    BitfieldEntry("orbitSource", slice(8, 11)),
    BitfieldEntry("ephAvail", 11),
    BitfieldEntry("almAvail", 12),
    BitfieldEntry("anoAvail", 13),
    BitfieldEntry("aopAvail", 14),
    BitfieldEntry("sbasCorrUsed", 16),
    BitfieldEntry("rtcmCorrUsed", 17),
    BitfieldEntry("prCorrUsed", 20),
    BitfieldEntry("crCorrUsed", 21),
    BitfieldEntry("doCorrUsed", 22),
    )
)

svs_fields = Fields(
    ("gnssId", U1),
    ("svId", U1),
    ("cno", U1),
    ("elev", I1),
    ("azim", I2),
    ("prRes", I2),
    ("flags", flags),
)

payload_description = Fields(
    ("iTOW", U4),
    ("version", U1),
    ("numSvs", U1),
    ("reserved1", 2*U1),
    ("meas", KeyLoop("numSvs", svs_fields))
)

description = MessageDescription(
    name="NAV-SAT",
    message_class=b"\x01",
    message_id=b"\x35",
    payload_description=Options(
        Empty,
        payload_description
    )
)
