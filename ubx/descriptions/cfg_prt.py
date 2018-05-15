from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("PortID", U1)
)

txReady = Bitfield(2, entries=[
    BitfieldEntry("en", 0),
    BitfieldEntry("pol", 1),
    BitfieldEntry("pin", slice(2, 7)),
    BitfieldEntry("thres", slice(7, 16))
])

mode = Bitfield(4, entries=[
    BitfieldEntry("charLen", slice(6, 8)),
    BitfieldEntry("parity", slice(9, 12)),
    BitfieldEntry("nStopBits", slice(12, 14))
])

inProtoMask = Bitfield(2, entries=[
    BitfieldEntry("inUbx", 0),
    BitfieldEntry("inNmea", 1),
    BitfieldEntry("inRtcm", 2),
    BitfieldEntry("inRtcm3", 5)
])

outProtoMask = Bitfield(2, entries=[
    BitfieldEntry("outUbx", 0),
    BitfieldEntry("outNmea", 1),
    BitfieldEntry("outRtcm3", 5)
])

flags = Bitfield(2, entries=[
    BitfieldEntry("extendedTxTimeout", 1)
])

payload_description1 = Fields(
    ("portID", U1),
    ("reserved1", U1),
    ("txReady", txReady),
    ("mode", mode),
    ("baudRate", U4),
    ("inProtoMask", inProtoMask),
    ("outProtoMask", outProtoMask),
    ("flags", flags),
    ("reserved2", List(2*[U1]))
)

payload_description2 = Fields(
    ("portID", U1),
    ("reserved1", U1),
    ("txReady", txReady),
    ("reserved2", mode),
    ("baudRate", U4),
    ("inProtoMask", inProtoMask),
    ("outProtoMask", outProtoMask),
    ("flags", flags),
    ("reserved2", List(2*[U1]))
)

description = MessageDescription(
    name="CFG-PRT",
    message_class=b"\x06",
    message_id=b"\x00",
    payload_description=Options(
        Empty,
        payload_description0,
        payload_description1,
    )
)
