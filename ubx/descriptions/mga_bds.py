from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description_eph = Fields(
    ("type", U1),
    ("version", U1),
    ("svId", U1),
    ("reserved1", U1),
    ("satH1", U1),
    ("IODC", U1),
    ("a2", I2),
    ("a1", I4),
    ("a0", I4),
    ("toc", U4),
    ("TGD1", I2),
    ("URAI", U1),
    ("IODE", U1),
    ("toe", U4),
    ("sqrtA", U4),
    ("e", U4),
    ("omega", I4),
    ("Deltan", I2),
    ("IDOT", I2),
    ("M0", I4),
    ("Omega0", I4),
    ("OmegaDot", I4),
    ("i0", I4),
    ("Cuc", I4),
    ("Cus", I4),
    ("Crc", I4),
    ("Crs", I4),
    ("Cic", I4),
    ("Cis", I4),
    ("reserved2", 4*U1)
)

payload_description_alm = Fields(
    ("type", U1),
    ("version", U1),
    ("svId", U1),
    ("reserved1", U1),
    ("Wna", U1),
    ("toa", U1),
    ("deltaI", I2),
    ("sqrtA", U4),
    ("e", U4),
    ("omega", I4),
    ("M0", I4),
    ("Omega0", I4),
    ("OmegaDot", I4),
    ("a0", I2),
    ("a1", I2),
    ("reserved2", 4*U1)
)

payload_description_health = Fields(
    ("type", U1),
    ("version", U1),
    ("reserved1", 2*U1),
    ("healthCode", 30*U2),
    ("reserved2", 4*U1)
)

payload_description_utc = Fields(
    ("type", U1),
    ("version", U1),
    ("reserved1", 2*U1),
    ("a0UTC", I4),
    ("a1UTC", I4),
    ("dtLS", I1),
    ("reserved2", U1),
    ("wnRec", U1),
    ("wnLSF", U1),
    ("dN", U1),
    ("dtLSF", I1),
    ("reserved3", 2*U1)
)

payload_description_iono = Fields(
    ("type", U1),
    ("version", U1),
    ("reserved1", 2*U1),
    ("alpha0", I1),
    ("alpha1", I1),
    ("alpha2", I1),
    ("alpha3", I1),
    ("beta0", I1),
    ("beta1", I1),
    ("beta2", I1),
    ("beta3", I1),
    ("reserved2", 4*U1)
)

description = MessageDescription(
    message_class=MGA,
    message_id=MessageId("BDS", b"\x03"),
    payload_description=Options(
        payload_description_eph,
        payload_description_alm,
        payload_description_health,
        payload_description_utc,
        payload_description_iono
    )
)
