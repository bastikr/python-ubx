from ..classid import *
from ..payload import *
from ..message import *


flags = Bitfield(2, entries=[
    BitfieldEntry("reEnum", 0),
    BitfieldEntry("powerMode", 1),
])

payload_description0 = Fields(
    ("vendorID", U2),
    ("productID", U2),
    ("reserved1", 2*U1),
    ("reserved2", 2*U1),
    ("powerConsumption", U2),
    ("flags", flags),
    ("vendorString", Chars(32)),
    ("productString", Chars(32)),
    ("serialNumber", Chars(32)),
)

description = MessageDescription(
    name="CFG-USB",
    message_class=CFG,
    message_id=b"\x1b",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
