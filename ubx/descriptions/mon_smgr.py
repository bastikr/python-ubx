from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


intOsc = Bitfield(2, entries=[
    BitfieldEntry("intOscState", slice(0, 4)),
    BitfieldEntry("intOscCalib", 4),
    BitfieldEntry("intOscDisc", 5)
])

extOsc = Bitfield(2, entries=[
    BitfieldEntry("extOscState", slice(0, 4)),
    BitfieldEntry("extOscCalib", 4),
    BitfieldEntry("extOscDisc", 5)
])

gnss = Bitfield(1, entries=[
    BitfieldEntry("gnssAvail", 0)
])

extInt0 = Bitfield(1, entries=[
    BitfieldEntry("extInt0Avail", 0),
    BitfieldEntry("extInt0Type", 1),
    BitfieldEntry("extInt0FeedBack", 2)
])

extInt1 = Bitfield(1, entries=[
    BitfieldEntry("extInt1Avail", 0),
    BitfieldEntry("extInt1Type", 1),
    BitfieldEntry("extInt1FeedBack", 2)
])

payload_description = Fields(
    ("version", U1),
    ("reserved1", 3*U1),
    ("iTOW", U4),
    ("intOsc", intOsc),
    ("extOsc", extOsc),
    ("discSrc", U1),
    ("gnss", gnss),
    ("extInt0", extInt0),
    ("extInt1", extInt1)
)

description = MessageDescription(
    message_class=MON,
    message_id=MessageId("SMGR", b"\x2e"),
    payload_description=Options(
        Empty,
        payload_description
    )
)
