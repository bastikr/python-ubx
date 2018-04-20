import struct
import codecs

from . import rawmessage
from . import checksum


class UBXReaderException(Exception):
    '''Ublox error class'''
    def __init__(self, msg):
        Exception.__init__(self, msg)
        self.message = msg

class UBXReader:
    def __init__(self, read):
        self.read = read

    def read_checked(self, n):
        buffer = self.read(n)
        if len(buffer)!=n:
            raise EOFError("Reached end of stream")
        return buffer

    def seek_syncchars(self):
        matched_syncchar1 = False
        while True:
            byte = self.read_checked(1)
            if matched_syncchar1:
                if byte == b"\x62":
                    return True
                else:
                    matched_syncchar1 = False
            if byte == b"\xb5":
                matched_syncchar1 = True

    def check_syncchars(self):
        byte = self.read_checked(1)
        if byte != b"\xb5":
            raise UBXReaderException("First syncchar is '{}' instead of 'b5'".format(codecs.encode(byte, "hex")))
        byte = self.read_checked(1)
        if byte != b"\x62":
            raise UBXReaderException("Second syncchar is '{}' instead of '62'".format(codecs.encode(byte, "hex")))

    def read_message_class(self):
        byte = self.read_checked(1)
        return byte

    def read_message_id(self):
        byte = self.read_checked(1)
        return byte

    def read_length(self):
        b = self.read_checked(2)
        return b

    def read_payload(self, length):
        b = self.read_checked(length)
        return b

    def read_checksumA(self):
        byte = self.read_checked(1)
        return byte

    def read_checksumB(self):
        byte = self.read_checked(1)
        return byte

    def read_rawmessage(self, seek_syncchars=True):
        if seek_syncchars:
            self.seek_syncchars()
        else:
            self.check_syncchars()
        byte_message_class = self.read_message_class()
        byte_message_id = self.read_message_id()
        byte_length = self.read_length()
        length = struct.unpack("<H", byte_length)[0]
        byte_payload = self.read_payload(length)
        byte_a = self.read_checksumA()
        byte_b = self.read_checksumB()
        try:
            int_a = struct.unpack("<B", byte_a)[0]
        except Exception as e:
            print("Length of byte_a: ", len(byte_a))
            print("Hex byte_a: ", codecs.encode(byte_a, "hex"))
            raise e
        int_b = struct.unpack("<B", byte_b)[0]
        checksum_received = checksum.Checksum(int_a, int_b)
        checksum_calculated = checksum.Checksum.from_bytestrings(byte_message_class, byte_message_id, byte_length, byte_payload)
        if checksum_received != checksum_calculated:
            raise UBXReaderException("Checksums don't match:\n"
                                     "    received   = {}\n"
                                     "    calculated = {}".format(
                                        checksum_received, checksum_calculated))
        return rawmessage.RawMessage(byte_message_class, byte_message_id, byte_payload)
