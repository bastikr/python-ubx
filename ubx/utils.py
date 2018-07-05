"""Module collecting several non-ubx related functions."""

import codecs


def byte2hexstring(byte):
    """
    Return a string containing the hex representation of a given byte.
    """
    if not isinstance(byte, bytes):
        raise TypeError("Expected argument \"byte\" to be of type \"bytes\" but it is of type \"{}\"".format(type(byte)))
    if len(byte)!=1:
        raise ValueError("Expected length of the given bytestring to by equal to 1.")
    return codecs.encode(byte, "hex").decode("utf-8")


def hexstring2byte(hexstring):
    """
    Return a byte corresponding to the given hex string.
    """
    if len(hexstring)!=2:
        raise ValueError("Expected length of the given hexstring to by equal to 2.")
    return codecs.decode(hexstring.encode("utf-8"), "hex")
