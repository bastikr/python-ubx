from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


mask = Bitfield(4, entries=[
    BitfieldEntry("ioPort", 0),
    BitfieldEntry("msgConf", 1),
    BitfieldEntry("infMsg", 2),
    BitfieldEntry("navConf", 3),
    BitfieldEntry("rxmConf", 4),
    BitfieldEntry("senConf", 8),
    BitfieldEntry("rinvConf", 9),
    BitfieldEntry("antConf", 10),
    BitfieldEntry("logConf", 11),
    BitfieldEntry("ftsConf", 12)
])

deviceMask = Bitfield(1, entries=[
    BitfieldEntry("devBBR", 0),
    BitfieldEntry("devFlash", 1),
    BitfieldEntry("devEEPROM", 2),
    BitfieldEntry("devSpiFlash", 4)
])

payload_description0 = Fields(
    ("clearMask", mask),
    ("saveMask", mask),
    ("loadMask", mask)
)

payload_description1 = Fields(
    ("clearMask", mask),
    ("saveMask", mask),
    ("loadMask", mask),
    ("deviceMask", deviceMask)
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("CFG", b"\x09"),
    payload_description=Options(
        payload_description0,
        payload_description1,
    )
)
