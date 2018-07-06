from ..message_class import *
from ..payload import *
from ..message import *


payload_description_pos_xyz = Fields(
    ("type", U1),
    ("version", U1),
    ("reserved1", 2*U1),
    ("ecefX", I4),
    ("ecefY", I4),
    ("ecefZ", I4),
    ("posAcc", U4)
)

payload_description_pos_llh = Fields(
    ("type", U1),
    ("version", U1),
    ("reserved1", 2*U1),
    ("lat", I4),
    ("lon", I4),
    ("alt", I4),
    ("posAcc", U4)
)

ref = Bitfield(1, entries=[
    BitfieldEntry("source", slice(0, 4)),
    BitfieldEntry("fall", 4),
    BitfieldEntry("last", 5)
])

payload_description_time_utc = Fields(
    ("type", U1),
    ("version", U1),
    ("ref", ref),
    ("leapSecs", I1),
    ("year", U2),
    ("month", U1),
    ("day", U1),
    ("hour", U1),
    ("minute", U1),
    ("second", U1),
    ("reserved1", U1),
    ("ns", U4),
    ("tAccS", U2),
    ("reserved2", 2*U1),
    ("tAccNs", U4),
)

payload_description_time_gps = Fields(
    ("type", U1),
    ("version", U1),
    ("ref", ref),
    ("gnssId", U1),
    ("reserved1", 2*U1),
    ("week", U2),
    ("tow", U4),
    ("ns", U4),
    ("tAccS", U2),
    ("reserved2", 2*U1),
    ("tAccNs", U4)
)

payload_description_clkd = Fields(
    ("type", U1),
    ("version", U1),
    ("reserved1", 2*U1),
    ("clkD", I4),
    ("clkDAcc", U4)
)

flags = Bitfield(1, entries=[
    BitfieldEntry("source", slice(0, 4)),
    BitfieldEntry("fall", 4)
])

payload_description_freq = Fields(
    ("type", U1),
    ("version", U1),
    ("reserved1", 2*U1),
    ("flags", flags),
    ("freq", I4),
    ("freqAcc", U4)
)

payload_description_eop = Fields(
    ("type", U1),
    ("version", U1),
    ("reserved1", 2*U1),
    ("d2kRef", U2),
    ("d2kMax", U2),
    ("xpP0", I4),
    ("xpP1", I4),
    ("ypP0", I4),
    ("ypP1", I4),
    ("dUT1", I4),
    ("ddUT1", I4),
    ("reserved2", 40*U1)
)

description = MessageDescription(
    name="MGA-INI",
    message_class=MGA,
    message_id=b"\x40",
    payload_description=Options(
        payload_description_pos_xyz,
        payload_description_pos_llh,
        payload_description_time_utc,
        payload_description_time_gps,
        payload_description_clkd,
        payload_description_freq,
        payload_description_eop
    )
)
