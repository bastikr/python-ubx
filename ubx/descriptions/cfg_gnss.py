from ..payload import *
from ..message import *


flags = Bitfield(4, [
    BitfieldEntry("enable", 0),
    BitfieldEntry("sigCfgMask", slice(16, 24))
])

cfgBlocks = Fields(
    ("gnssId", U1),
    ("resTrkCh", U1),
    ("maxTrkCh", U1),
    ("reserved1", U1),
    ("flags", flags)
)

payload_description0 = Fields(
    ("msgVer", U1),
    ("numTrkChHw", U1),
    ("numTrkChUse", U1),
    ("numCfgBlocks", U1),
    ("cfgBlocks", KeyLoop("numCfgBlocks", cfgBlocks))
)

description = MessageDescription(
    name="CFG-GNSS",
    message_class=b"\x06",
    message_id=b"\x3e",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)
