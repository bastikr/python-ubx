import codecs

def byte2hexstring(byte):
    assert isinstance(byte, bytes)
    return codecs.encode(byte, "hex").decode("utf-8")
