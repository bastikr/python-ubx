from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


flags_0 = Bitfield(4, [
    BitfieldEntry("backup", 1)
])

payload_description0 = Fields(
    ("duration", U4),
    ("flags", flags_0),
)


flags_1 = Bitfield(4, [
    BitfieldEntry("backup", 1),
    BitfieldEntry("force", 2)
])

wakeupSources = Bitfield(4, [
    BitfieldEntry("uartrx", 3),
    BitfieldEntry("extint0", 5),
    BitfieldEntry("extint1", 6),
    BitfieldEntry("spics", 7)
])

payload_description1 = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("duration", U4),
    ("flags", flags_1),
    ("wakeupSources", wakeupSources)
)

description = MessageDescription(
    message_class=RXM,
    message_id=MessageId("PMREQ", b"\x41"),
    payload_description=Options(
        Empty,
        payload_description0,
        payload_description1
    )
)
