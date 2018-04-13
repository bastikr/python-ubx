import unittest

from ubx import checksum

class TestChecksum(unittest.TestCase):
    def test_checksum(self):
        c = checksum.Checksum.from_bytestrings(b"\x0f")
        print(c)

if __name__ == '__main__':
    unittest.main()
