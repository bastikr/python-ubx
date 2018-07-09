import unittest

import ubx


class TestMessageClass(unittest.TestCase):
    def test_creation(self):
        m = ubx.MessageClass("TEST", b"\x01")
        self.assertEqual(m.name, "TEST")
        self.assertEqual(m.byte, b"\x01")

        with self.assertRaises(TypeError):
            ubx.MessageClass("TEST", 1)

    def test_equality(self):
        m0 = ubx.MessageClass("TEST", b"\x01")
        m1 = ubx.MessageClass("TEST", b"\x01")
        m2 = ubx.MessageClass("TEST2", b"\x01")
        m3 = ubx.MessageClass("TEST", b"\x02")
        self.assertTrue(m0==m0)
        self.assertTrue(m0==m1)
        self.assertTrue(m2==m2)
        self.assertTrue(m3==m3)
        self.assertFalse(m0!=m0)
        self.assertFalse(m0!=m1)
        self.assertFalse(m2!=m2)
        self.assertFalse(m3!=m3)

        self.assertFalse(m0==m2)
        self.assertFalse(m0==m3)
        self.assertTrue(m0!=m2)
        self.assertTrue(m0!=m3)

    def test_repr(self):
        m = ubx.MessageClass("TEST", b"\x01")
        self.assertEqual(str(m), "MessageClass(name=TEST, byte=0x01)")

    def test_getbyname(self):
        m = ubx.MessageClass("NAV", b"\x01")
        self.assertEqual(m, ubx.message_class.get_by_name("NAV"))
        with self.assertRaises(ValueError):
            ubx.message_class.get_by_name("FOO")

    def test_getbybyte(self):
        m = ubx.MessageClass("NAV", b"\x01")
        self.assertEqual(m, ubx.message_class.get_by_byte(b"\x01"))
        with self.assertRaises(TypeError):
            ubx.message_class.get_by_byte(1)
        with self.assertRaises(ValueError):
            ubx.message_class.get_by_byte(b"\xfe")


if __name__ == '__main__':
    unittest.main()
