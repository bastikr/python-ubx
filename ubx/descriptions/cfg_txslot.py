from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


enable = Bitfield(1, entries=[
    BitfieldEntry("DDC", 0),
    BitfieldEntry("UART1", 1),
    BitfieldEntry("UART2", 2),
    BitfieldEntry("USB", 3),
    BitfieldEntry("SPI", 4)
])

payload_description0 = Fields(
    ("version", U1),
    ("enable", enable),
    ("refTp", U1),
    ("reserved1", U1),
    ("end", 4*U4)
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("TXSLOT", b"\x53"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
