import unittest
import ubx


class TestByteHexConversion(unittest.TestCase):
    def test_conversion(self):
        byte = b"\x03"
        hexstring = ubx.utils.byte2hexstring(byte)
        self.assertEqual(hexstring, "03")
        self.assertEqual(byte, ubx.utils.hexstring2byte(hexstring))

    def test_exceptions_hexstring2bytestring(self):
        with self.assertRaises(TypeError):
            ubx.utils.byte2hexstring(u"a")
        with self.assertRaises(TypeError):
            ubx.utils.byte2hexstring(3)
        with self.assertRaises(ValueError):
            ubx.utils.byte2hexstring(b"\x04\x03")

    def test_exceptions_bytestring2hexstring(self):
        with self.assertRaises(ValueError):
            ubx.utils.hexstring2byte("4512")


if __name__ == '__main__':
    unittest.main()
