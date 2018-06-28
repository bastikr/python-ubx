from ..classid import *
from ..payload import *
from ..message import *


flags = Bitfield(4, entries=[
    BitfieldEntry("leapNow", 0),
    BitfieldEntry("leapSoon", 1),
    BitfieldEntry("leapPositive", 2),
    BitfieldEntry("timeInLimit", 3),
    BitfieldEntry("intOscInLimit", 4),
    BitfieldEntry("extOscInLimit", 5),
    BitfieldEntry("gnssTimeValid", 6),
    BitfieldEntry("UTCTimeValid", 7),
    BitfieldEntry("DiscSrc", slice(8, 11)),
    BitfieldEntry("raim", 11),
    BitfieldEntry("cohPulse", 12),
    BitfieldEntry("lockedPulse", 13),
])

payload_description = Fields(
    ("version", U1),
    ("gnssId", U1),
    ("reserved1", 2*U1),
    ("flags", flags),
    ("year", U2),
    ("month", U1),
    ("day", U1),
    ("hour", U1),
    ("minute", U1),
    ("second", U1),
    ("utcStandard", U1),
    ("utcOffset", I4),
    ("utcUncertainty", U4),
    ("week", U4),
    ("TOW", U4),
    ("gnssOffset", I4),
    ("gnssUncertainty", U4),
    ("intOscOffset", I4),
    ("intOscUncertainty", U4),
    ("extOscOffset", I4),
    ("extOscUncertainty", U4)
)

description = MessageDescription(
    name="TIM-TOS",
    message_class=TIM,
    message_id=b"\x12",
    payload_description=Options(
        Empty,
        payload_description
    )
)
