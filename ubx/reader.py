import struct

from . import utils
from . import rawmessage
from . import checksum


class ReaderException(Exception):
    '''Ublox error class'''
    def __init__(self, msg):
        Exception.__init__(self, msg)
        self.message = msg


class Reader:
    def __init__(self, read):
        self.read = read

    def read_checked(self, n):
        buffer = self.read(n)
        if len(buffer) != n:
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
            raise ReaderException(
                "First syncchar is '{}' instead of 'b5'".format(
                    utils.byte2hexstring(byte)))
        byte = self.read_checked(1)
        if byte != b"\x62":
            raise ReaderException(
                "Second syncchar is '{}' instead of '62'".format(
                    utils.byte2hexstring(byte)))

    def read_rawmessageparts(self, seek_syncchars=True):
        if seek_syncchars:
            self.seek_syncchars()
        else:
            self.check_syncchars()
        header = self.read_checked(4)
        byte_message_class = header[0:1]
        byte_message_id = header[1:2]
        bytes_length = header[2:4]

        length = struct.unpack("<H", bytes_length)[0]
        bytes_payload = self.read_checked(length)

        bytes_checksum = self.read_checked(2)
        int_a, int_b = struct.unpack("<BB", bytes_checksum)
        checksum_received = checksum.Checksum(int_a, int_b)
        checksum_calculated = checksum.Checksum.from_bytestrings(
            byte_message_class, byte_message_id, bytes_length, bytes_payload)
        checksum_received.check_equal(checksum_calculated)
        return (byte_message_class, byte_message_id,
                bytes_length, bytes_payload, bytes_checksum)

    def read_rawmessage(self, seek_syncchars=True):
        parts = self.read_rawmessageparts(seek_syncchars=seek_syncchars)
        byte_message_class, byte_message_id, _, bytes_payload, _ = parts
        return rawmessage.RawMessage(byte_message_class, byte_message_id, bytes_payload)
