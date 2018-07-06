import unittest

import ubx


class TestChecksum(unittest.TestCase):
    def test_creation(self):
        c = ubx.Checksum(1, 2)
        self.assertEqual(c.a, 1)
        self.assertEqual(c.b, 2)

        c = ubx.Checksum(257, 258)
        self.assertEqual(c.a, 1)
        self.assertEqual(c.b, 2)

        a = 256**20 + 7
        b = 256**15 + 3
        c = ubx.Checksum(a, b)
        self.assertEqual(c.a, 7)
        self.assertEqual(c.b, 3)

        with self.assertRaises(TypeError):
            ubx.Checksum(b"\x31", 1)
        with self.assertRaises(TypeError):
            ubx.Checksum(1, b"\x31")
        with self.assertRaises(TypeError):
            ubx.Checksum(b"\x31", b"\x02")

    def test_frombytestring(self):
        c = ubx.Checksum.from_bytestrings(b"\xfe", b"\x0f", b"\x05")
        a = (254 + 15 + 5) % 256
        b = (254*3 + 15*2 + 5) % 256
        self.assertEqual(c.a, a)
        self.assertEqual(c.b, b)

    def test_update(self):
        c = ubx.Checksum(254, 254)
        c.update(b"\x0f")
        c.update(b"\x05")
        a = (254 + 15 + 5) % 256
        b = (254*3 + 15*2 + 5) % 256
        self.assertEqual(c.a, a)
        self.assertEqual(c.b, b)

    def test_equality(self):
        c0 = ubx.Checksum(2, 5)
        c1 = ubx.Checksum(2, 6)
        c2 = ubx.Checksum(1, 5)

        self.assertTrue(c0==c0)
        self.assertFalse(c0!=c0)
        self.assertTrue(c1==c1)
        self.assertFalse(c1!=c1)
        self.assertTrue(c2==c2)
        self.assertFalse(c2!=c2)

        self.assertFalse(c0==c1)
        self.assertFalse(c0==c2)
        self.assertFalse(c1==c2)

    def test_bytes(self):
        c = ubx.Checksum.from_bytestrings(b"\xfe", b"\x0f", b"\x05")
        self.assertEqual(c.bytes(), b"\x12\x1d")

    def test_check_equal(self):
        with self.assertRaises(ubx.ChecksumError):
            ubx.Checksum(0, 1).check_equal(ubx.Checksum(0, 0))


if __name__ == '__main__':
    unittest.main()
