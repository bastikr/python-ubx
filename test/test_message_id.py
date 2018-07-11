import unittest

import ubx


class TestMessageId(unittest.TestCase):
    def test_creation(self):
        m = ubx.MessageId("TEST", b"\x01")
        self.assertEqual(m.name, "TEST")
        self.assertEqual(m.byte, b"\x01")

        with self.assertRaises(TypeError):
            ubx.MessageId("TEST", 1)

    def test_equality(self):
        m0 = ubx.MessageId("TEST", b"\x01")
        m1 = ubx.MessageId("TEST", b"\x01")
        m2 = ubx.MessageId("TEST", b"\x01", "SUB")
        m3 = ubx.MessageId("TEST", b"\x02")
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
        m = ubx.MessageId("TEST", b"\x01")
        self.assertEqual(str(m), "MessageId(name=TEST, byte=0x01)")
        m = ubx.MessageId("TEST", b"\x01", "SUB")
        self.assertEqual(str(m), "MessageId(name=TEST, subname=SUB, byte=0x01)")


if __name__ == '__main__':
    unittest.main()
