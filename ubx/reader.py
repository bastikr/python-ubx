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
            raise UBXReaderException("First syncchar is '{}' instead of 'b5'".format(
                                        codecs.encode(byte, "hex").decode("utf-8")))
        byte = self.read_checked(1)
        if byte != b"\x62":
            raise UBXReaderException("Second syncchar is '{}' instead of '62'".format(
                                        codecs.encode(byte, "hex").decode("utf-8")))

    def read_rawmessage(self, seek_syncchars=True):
        if seek_syncchars:
            self.seek_syncchars()
        else:
            self.check_syncchars()
        header = self.read_checked(4)
        byte_message_class = header[0:1]
        byte_message_id = header[1:2]
        byte_length = header[2:4]

        length = struct.unpack("<H", byte_length)[0]
        bytes_payload = self.read_checked(length)

        bytes_checksum = self.read_checked(2)
        int_a, int_b = struct.unpack("<BB", bytes_checksum)
        checksum_received = checksum.Checksum(int_a, int_b)
        checksum_calculated = checksum.Checksum.from_bytestrings(byte_message_class, byte_message_id, byte_length, bytes_payload)
        checksum_received.check_equal(checksum_calculated)
        return rawmessage.RawMessage(byte_message_class, byte_message_id, bytes_payload)
