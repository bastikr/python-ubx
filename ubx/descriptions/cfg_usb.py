from ..payload import *
from ..message import *


flags = Bitfield(2, entries=[
    BitfieldEntry("reEnum", 0),
    BitfieldEntry("powerMode", 1),
])

payload_description0 = Fields(
    ("vendorID", U2),
    ("productID", U2),
    ("reserved1", List(2*[U1])),
    ("reserved2", List(2*[U1])),
    ("powerConsumption", U2),
    ("flags", flags),
    ("vendorString", List(32*[U1])),
    ("productString", List(32*[U1])),
    ("serialNumber", List(32*[U1])),
)

description = MessageDescription(
    name="CFG-USB",
    message_class=b"\x06",
    message_id=b"\x1b",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
