import codecs


def byte2hexstring(byte):
    if not isinstance(byte, bytes):
        raise TypeError("Expected argument \"byte\" to be of type \"bytes\" but it is of type \"{}\"".format(type(byte)))
    return codecs.encode(byte, "hex").decode("utf-8")


def hexstring2byte(hexstring):
    return codecs.decode(hexstring.encode("utf-8"), "hex")
