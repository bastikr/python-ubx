import unittest

import ubx
from ubx.descriptions import mon_hw
from ubx.descriptions import rxm_rawx


class TestPrinting(unittest.TestCase):
    def test_AtomicVariable(self):
        self.assertEqual(str(ubx.U1), "U1")
        self.assertEqual(str(ubx.U2), "U2")
        self.assertEqual(str(ubx.U4), "U4")
        self.assertEqual(str(ubx.U8), "U8")

        self.assertEqual(str(ubx.I1), "I1")
        self.assertEqual(str(ubx.I2), "I2")
        self.assertEqual(str(ubx.I4), "I4")
        self.assertEqual(str(ubx.I8), "I8")

        self.assertEqual(str(ubx.X1), "Bitfield(1)")
        self.assertEqual(str(ubx.X2), "Bitfield(2)")
        self.assertEqual(str(ubx.X4), "Bitfield(4)")
        self.assertEqual(str(ubx.X8), "Bitfield(8)")

        self.assertEqual(str(ubx.R4), "R4")
        self.assertEqual(str(ubx.R8), "R8")


class TestDescriptions(unittest.TestCase):
    def test_parse(self):
        print(rxm_rawx.description)

if __name__ == '__main__':
    unittest.main()
