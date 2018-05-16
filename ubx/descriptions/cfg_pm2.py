from ..payload import *
from ..message import *


flags0 = Bitfield(4, entries=[
    BitfieldEntry("extintSel", 4),
    BitfieldEntry("extintWake", 5),
    BitfieldEntry("extintBackup", 6),
    BitfieldEntry("limitPeakCurr", slice(8, 10)),
    BitfieldEntry("waitTimeFix", 10),
    BitfieldEntry("updateRTC", 11),
    BitfieldEntry("updateEPH", 12),
    BitfieldEntry("doNotEnterOff", 16),
    BitfieldEntry("mode", slice(17, 19)),
])

payload_description0 = Fields(
    ("version", U1),
    ("reserved1", U1),
    ("maxStartupStateDur", U1),
    ("reserved2", U1),
    ("flags", flags0),
    ("updatePeriod", U4),
    ("searchPeriod", U4),
    ("gridOffset", U4),
    ("onTime", U2),
    ("minAcqTime", U2),
    ("reserved3", List(20*[U1])),
)


flags1 = Bitfield(4, entries=[
    BitfieldEntry("optTarget", slice(1, 4)),
    BitfieldEntry("extintSel", 4),
    BitfieldEntry("extintWake", 5),
    BitfieldEntry("extintBackup", 6),
    BitfieldEntry("extintInactive", 7),
    BitfieldEntry("limitPeakCurr", slice(8, 10)),
    BitfieldEntry("waitTimeFix", 10),
    BitfieldEntry("updateRTC", 11),
    BitfieldEntry("updateEPH", 12),
    BitfieldEntry("doNotEnterOff", 16),
    BitfieldEntry("mode", slice(17, 19)),
])

payload_description1 = Fields(
    ("version", U1),
    ("reserved1", U1),
    ("maxStartupStateDur", U1),
    ("reserved2", U1),
    ("flags", flags1),
    ("updatePeriod", U4),
    ("searchPeriod", U4),
    ("gridOffset", U4),
    ("onTime", U2),
    ("minAcqTime", U2),
    ("reserved3", List(20*[U1])),
    ("extintInactivityMs", U4)
)



description = MessageDescription(
    name="CFG-PM2",
    message_class=b"\x06",
    message_id=b"\x3b",
    payload_description=Options(
        Empty,
        payload_description0,
        payload_description1,
    )
)
