from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description_eph = Fields(
    ("type", U1),
    ("version", U1),
    ("svId", U1),
    ("reserved1", U1),
    ("iodNav", U2),
    ("deltaN", I2),
    ("m0", I4),
    ("e", U4),
    ("sqrtA", U4),
    ("omega0", I4),
    ("i0", I4),
    ("omega", I4),
    ("omegaDot", I4),
    ("iDot", I2),
    ("cuc", I2),
    ("cus", I2),
    ("crc", I2),
    ("crs", I2),
    ("cic", I2),
    ("cis", I2),
    ("toe", U2),
    ("af0", I4),
    ("af1", I4),
    ("af2", I1),
    ("sisaIndexE1E5b", U1),
    ("toc", U2),
    ("bgdE1E5b", I2),
    ("reserved2", 2*U1),
    ("healthE1b", U1),
    ("dataValidityE1b", U1),
    ("healthE5b", U1),
    ("dataValidityE5b", U1),
    ("reserved3", 4*U1)
)

payload_description_alm = Fields(
    ("type", U1),
    ("version", U1),
    ("svId", U1),
    ("reserved1", U1),
    ("ioda", U1),
    ("almWNa", U1),
    ("toa", U2),
    ("deltaSqrtA", I2),
    ("e", U2),
    ("deltaI", I2),
    ("omega0", I2),
    ("omegaDot", I2),
    ("omega", I2),
    ("m0", I2),
    ("af0", I2),
    ("af1", I2),
    ("healthE1B", U1),
    ("healthE5b", U1),
    ("reserved2", 4*U1)
)

payload_description_timeoffset = Fields(
    ("type", U1),
    ("version", U1),
    ("reserved1", 2*U1),
    ("a0G", I2),
    ("a1G", I2),
    ("t0G", U1),
    ("wn0G", U1),
    ("reserved2", 2*U1)
)

payload_description_utc = Fields(
    ("type", U1),
    ("version", U1),
    ("reserved1", 2*U1),
    ("a0", I4),
    ("a1", I4),
    ("dtLS", I1),
    ("tot", U1),
    ("wnt", U1),
    ("wnLSF", U1),
    ("dN", U1),
    ("dtLSF", I1),
    ("reserved2", 2*U1)
)

description = MessageDescription(
    message_class=MGA,
    message_id=MessageId("GAL", b"\x02"),
    payload_description=Options(
        payload_description_eph,
        payload_description_alm,
        payload_description_timeoffset,
        payload_description_utc
    )
)
