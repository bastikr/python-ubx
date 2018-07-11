from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


mask1 = Bitfield(2, entries=[
    BitfieldEntry("minMax", 2),
    BitfieldEntry("minCno", 3),
    BitfieldEntry("initial3dfix", 6),
    BitfieldEntry("wknRoll", 9),
    BitfieldEntry("ackAid", 10),
    BitfieldEntry("ppp", 13),
    BitfieldEntry("aop", 14),
])

mask2_0 = Bitfield(4, entries=[
    BitfieldEntry("adr", 6)
])

aopCfg = Bitfield(1, entries=[
    BitfieldEntry("useAOP", 0)
])

# Version 15 - 17
payload_description0 = Fields(
    ("version", U2),
    ("mask1", mask1),
    ("mask2", mask2_0),
    ("reserved1", 2*U1),
    ("minSVs", U1),
    ("maxSVs", U1),
    ("minCNO", U1),
    ("reserved2", U1),
    ("iniFix3D", U1),
    ("reserved3", 2*U1),
    ("ackAiding", U1),
    ("wknRollover", U2),
    ("reserved4", 6*U1),
    ("usePPP", U1),
    ("aopCfg", aopCfg),
    ("reserved5", 2*U1),
    ("aopOrbMaxErr", U2),
    ("reserved6", 4*U1),
    ("reserved7", 3*U1),
    ("useAddr", U1)
)


mask2_1 = Bitfield(4, entries=[
    BitfieldEntry("adr", 6),
    BitfieldEntry("sigAttenComp", 6)
])

# Version 18 - 23.01
payload_description1 = Fields(
    ("version", U2),
    ("mask1", mask1),
    ("mask2", mask2_1),
    ("reserved1", 2*U1),
    ("minSVs", U1),
    ("maxSVs", U1),
    ("minCNO", U1),
    ("reserved2", U1),
    ("iniFix3D", U1),
    ("reserved3", 2*U1),
    ("ackAiding", U1),
    ("wknRollover", U2),
    ("sigAttenCompMode", U1),
    ("reserved4", U1),
    ("reserved5", 2*U1),
    ("reserved6", 2*U1),
    ("usePPP", U1),
    ("aopCfg", aopCfg),
    ("reserved7", 2*U1),
    ("aopOrbMaxErr", U2),
    ("reserved8", 4*U1),
    ("reserved9", 3*U1),
    ("useAddr", U1)
)


# Version 19.1
payload_description2 = Fields(
    ("version", U2),
    ("mask1", mask1),
    ("mask2", mask2_1),
    ("reserved1", 2*U1),
    ("minSVs", U1),
    ("maxSVs", U1),
    ("minCNO", U1),
    ("reserved2", U1),
    ("iniFix3D", U1),
    ("reserved3", 2*U1),
    ("ackAiding", U1),
    ("wknRollover", U2),
    ("sigAttenCompMode", U1),
    ("reserved4", U1),
    ("reserved5", 2*U1),
    ("reserved6", 2*U1),
    ("usePPP", U1),
    ("aopCfg", aopCfg),
    ("reserved7", 2*U1),
    ("aopOrbMaxErr", U2),
    ("reserved8", 4*U1),
    ("reserved9", 3*U1),
    ("useAddr", U1),
    ("reserved10", 2*U1),
    ("reserved11", 2*U1)
)


description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("NAVX5", b"\x23"),
    payload_description=Options(
        Empty,
        payload_description2,
        payload_description1,
        payload_description0
    )
)
