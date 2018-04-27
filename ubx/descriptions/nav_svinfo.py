from ..payload import *
from ..message import *


chn_fields = Fields(
  ("chn", U1),
  ("svid", U1),
  ("flags", X1),
  ("quality", X1),
  ("cno", U1),
  ("elev", I1),
  ("azim", I2),
  ("prRes", I4)
)

payload_description0 = Fields(
    ("iTOW", U4),
    ("numCh", U1),
    ("globalFlags", X1),
    ("reserved1", List(2*[U1])),
    ("ch", Loop("numCh", chn_fields)),
)

description = MessageDescription(
    name="NAV-SVINFO",
    message_class=b"\x01",
    message_id=b"\x30",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
