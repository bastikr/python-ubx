from ..classid import *
from ..payload import *
from ..message import *


payload_description = MatchedLoop(
    Fields(
        ("rxBytes", U4),
        ("txBytes", U4),
        ("parityErrs", U2),
        ("framingErrs", U2),
        ("overrunErrs", U2),
        ("breakCond", U2),
        ("rxBusy", U1),
        ("txBusy", U1),
        ("reserved1", 2*U1)
    )
)

description = MessageDescription(
    name="MON-IO",
    message_class=MON,
    message_id=b"\x02",
    payload_description=Options(
        Empty,
        payload_description
    )
)
