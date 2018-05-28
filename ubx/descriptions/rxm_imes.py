from ..classid import *
from ..payload import *
from ..message import *


position1_1 = Bitfield(4, [
    BitfieldEntry("pos1Floor", slice(0, 8)),
    BitfieldEntry("pos1Lat", slice(8, 31))
])

position1_2 = Bitfield(4, [
    BitfieldEntry("pos1Lon", slice(0, 24)),
    BitfieldEntry("pos1Valid", 24)
])

position2_1 = Bitfield(4, [
    BitfieldEntry("pos2Floor", slice(0, 9)),
    BitfieldEntry("pos2Alt", slice(9, 21)),
    BitfieldEntry("pos2Acc", slice(21, 23)),
    BitfieldEntry("pos1Valid", 23)
])

shortIdFrame = Bitfield(4, [
    BitfieldEntry("shortId", slice(0, 12)),
    BitfieldEntry("shortValid", 12),
    BitfieldEntry("shortBoundary", 13)
])

mediumId_2 = Bitfield(4, [
    BitfieldEntry("mediumIdMSB", 0),
    BitfieldEntry("mediumValid", 1),
    BitfieldEntry("mediumboundary", 2)
])

tx = Fields(
    ("reserved2", U1),
    ("txId", U1),
    ("reserved3", 3*U1),
    ("cno", U1),
    ("reserved4", 2*U1),
    ("doppler", I4),
    ("position1_1", position1_1),
    ("position1_2", position1_2),
    ("position2_1", position2_1),
    ("lat", I4),
    ("lon", I4),
    ("shortIdFrame", shortIdFrame),
    ("mediumIdLSB", U4),
    ("mediumId_2", mediumId_2)
)

payload_description0 = Fields(
    ("numTx", U1),
    ("version", U1),
    ("resreved1", 2*U1),
    ("txs", KeyLoop("numTx", tx))
)

description = MessageDescription(
    name="RXM-IMES",
    message_class=RXM,
    message_id=b"\x61",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
