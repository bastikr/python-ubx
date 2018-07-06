from ..message_class import *
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

# mode_uart = Bitfield(4, entries=[
#     BitfieldEntry("charLen", slice(6, 8)),
#     BitfieldEntry("parity", slice(9, 12)),
#     BitfieldEntry("nStopBits", slice(12, 14))
# ])

# mode_usb = 8*U1

# mode_spi = Bitfield(2, entries=[
#     BitfieldEntry("spiMode", slice(1, 3)),
#     BitfieldEntry("ffCnt", slice(8, 14))
# ])

# mode_ddc = Bitfield(2, entries=[
#     BitfieldEntry("slaveAddr", slice(1, 8))
# ])

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
    ("mode", X4),
    ("baudRate", U4),
    ("inProtoMask", inProtoMask),
    ("outProtoMask", outProtoMask),
    ("flags", flags),
    ("reserved2", 2*U1)
)


description = MessageDescription(
    name="CFG-PRT",
    message_class=CFG,
    message_id=b"\x00",
    payload_description=Options(
        payload_description0,
        payload_description1
    )
)
