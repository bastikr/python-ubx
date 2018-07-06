from ..message_class import *
from ..payload import *
from ..message import *


payload_description = Fields(
    ("entryIndex", U4),
    ("lon", I4),
    ("lat", I4),
    ("hMSL", I4),
    ("hAcc", U4),
    ("gSpeed", U4),
    ("heading", U4),
    ("version", U1),
    ("fixType", U1),
    ("year", U2),
    ("month", U1),
    ("day", U1),
    ("hour", U1),
    ("minute", U1),
    ("second", U1),
    ("reserved1", U1),
    ("numSV", U1),
    ("reserved2", U1)
)

description = MessageDescription(
    name="LOG-RETRIEVEPOS",
    message_class=LOG,
    message_id=b"\x0b",
    payload_description=Options(
        payload_description
    )
)
