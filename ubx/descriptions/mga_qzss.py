from ..message_class import *
from ..payload import *
from ..message import *


payload_description_eph = Fields(
    ("type", U1),
    ("version", U1),
    ("svId", U1),
    ("reserved1", U1),
    ("fitInterval", U1),
    ("uraIndex", U1),
    ("svHealth", U1),
    ("tgd", I1),
    ("iodc", U2),
    ("toc", U2),
    ("reserved2", U1),
    ("af2", I1),
    ("af1", I2),
    ("af0", I4),
    ("crs", I2),
    ("deltaN", I2),
    ("m0", I4),
    ("cuc", I2),
    ("cus", I2),
    ("e", U4),
    ("sqrtA", U4),
    ("toe", U2),
    ("cic", I2),
    ("omega0", I4),
    ("cis", I2),
    ("crc", I2),
    ("i0", I4),
    ("omega", I4),
    ("omegaDot", I4),
    ("idot", I2),
    ("reserved3", 2*U1)
)

payload_description_alm = Fields(
    ("type", U1),
    ("version", U1),
    ("svId", U1),
    ("svHealth", U1),
    ("e", U2),
    ("almWNa", U1),
    ("toa", U1),
    ("deltaI", I2),
    ("omegaDot", I2),
    ("sqrtA", U4),
    ("omega0", I4),
    ("omega", I4),
    ("m0", I4),
    ("af0", I2),
    ("af1", I2),
    ("reserved1", 4*U1)
)

payload_description_health = Fields(
    ("type", U1),
    ("version", U1),
    ("reserved1", 2*U1),
    ("healthCode", 5*U1),
    ("reserved2", 3*U1)
)

description = MessageDescription(
    name="MGA-QZSS",
    message_class=MGA,
    message_id=b"\x05",
    payload_description=Options(
        payload_description_eph,
        payload_description_alm,
        payload_description_health,
    )
)
