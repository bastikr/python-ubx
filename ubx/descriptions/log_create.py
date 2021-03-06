from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


logCfg = Bitfield(1, entries=[
    BitfieldEntry("circular", 0)
])

payload_description = Fields(
    ("version", U1),
    ("logCfg", logCfg),
    ("reserved1", U1),
    ("logSize", U1),
    ("userDefinedSize", U4)
)

description = MessageDescription(
    message_class=LOG,
    message_id=MessageId("CREATE", b"\x07"),
    payload_description=Options(
        payload_description
    )
)
