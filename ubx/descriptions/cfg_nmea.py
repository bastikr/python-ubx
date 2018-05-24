from ..payload import *
from ..message import *


filterflags = Bitfield(1, entries=[
    BitfieldEntry("posFilt", 0),
    BitfieldEntry("mskPosFilt", 1),
    BitfieldEntry("timeFilt", 2),
    BitfieldEntry("dateFilt", 3),
    BitfieldEntry("gpsOnlyFilter", 4),
    BitfieldEntry("trackFilt", 5),
])

flags = Bitfield(1, entries=[
    BitfieldEntry("compat", 0),
    BitfieldEntry("consider", 1),
    BitfieldEntry("limit82", 2),
    BitfieldEntry("highPrec", 3)
])

gnssToFilter = Bitfield(4, entries=[
    BitfieldEntry("gps", 0),
    BitfieldEntry("sbas", 1),
    BitfieldEntry("qzss", 4),
    BitfieldEntry("glonass", 5),
    BitfieldEntry("beidou", 6),
])

payload_description0 = Fields(
    ("filter", filterflags),
    ("nmeaVersion", U1),
    ("numSV", U1),
    ("flags", flags)
)

payload_description1 = Fields(
    ("filter", filterflags),
    ("nmeaVersion", U1),
    ("numSV", U1),
    ("flags", flags),
    ("gnssToFilter", gnssToFilter),
    ("svNumbering", U1),
    ("mainTalkerIf", U1),
    ("gsvTalkerId", U1),
    ("version", U1),
)

payload_description2 = Fields(
    ("filter", filterflags),
    ("nmeaVersion", U1),
    ("numSV", U1),
    ("flags", flags),
    ("gnssToFilter", gnssToFilter),
    ("svNumbering", U1),
    ("mainTalkerIf", U1),
    ("gsvTalkerId", U1),
    ("version", U1),
    ("bdsTalkerId", Chars(2)),
    ("reserved1", 6*U1)
)

description = MessageDescription(
    name="CFG-NMEA",
    message_class=b"\x06",
    message_id=b"\x17",
    payload_description=Options(
        Empty,
        payload_description0,
        payload_description1,
        payload_description2
    )
)
