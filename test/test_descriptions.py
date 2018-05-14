import unittest

import os
import codecs

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

    def test_List(self):
        self.assertEqual(str(ubx.List(["a", "b"])), "[\n  a,\n  b\n]")
        self.assertEqual(str(ubx.List(["a", ubx.List("b")])),
                        "[\n"
                        "  a,\n"
                        "  [\n"
                        "    b\n"
                        "  ]\n"
                        "]")

    def test_Fields(self):
        field1 = ("a", "va")
        field2 = ("b", "vb")
        field3 = ("c", "vc")
        fields1 = ubx.Fields(field1, field2)
        self.assertEqual(str(fields1),
                        "Fields(length=?) {\n"
                        "  a: va,\n"
                        "  b: vb\n"
                        "}")
        fields2 = ubx.Fields(("fields", fields1), field3)
        self.assertEqual(str(fields2),
                        "Fields(length=?) {\n"
                        "  fields:\n"
                        "    Fields(length=?) {\n"
                        "      a: va,\n"
                        "      b: vb\n"
                        "    },\n"
                        "  c: vc\n"
                        "}")

    def test_Loop(self):
        field1 = ("a", "va")
        field2 = ("b", "vb")
        field3 = ("c", "vc")
        self.assertEqual(str(ubx.Loop("k", "va")),
                        "Loop(key=\"k\"):\n"
                        "| va")
        self.assertEqual(str(ubx.Loop("k", ubx.Fields(field1, field2, field3))),
                        "Loop(key=\"k\"):\n"
                        "| Fields(length=?) {\n"
                        "|   a: va,\n"
                        "|   b: vb,\n"
                        "|   c: vc\n"
                        "| }")



class TestDescriptions(unittest.TestCase):
    pass


def make_testfunc(directory, name):
    _, message_class, message_id, length, checksum = name[:-4].split("-")
    message_class = codecs.decode(message_class.encode("utf-8"), "hex")
    message_id = codecs.decode(message_id.encode("utf-8"), "hex")
    checksum = codecs.decode(checksum.encode("utf-8"), "hex")
    def test(self):
        with open(os.path.join(directory, name), "rb") as f:
            reader = ubx.Reader(f.read)
            msg = reader.read_rawmessage()
        self.assertEqual(message_class, msg.message_class)
        self.assertEqual(message_id, msg.message_id)
        self.assertEqual(int(length), len(msg))
        self.assertEqual(checksum, msg.checksum().bytes())
    return test


testdir = "../ubx-testdata/data"
names = os.listdir(testdir)
for name in names:
    if not name.endswith("ubx"):
        continue
    f = make_testfunc(testdir, name)
    setattr(TestDescriptions, 'test_{0}'.format(name[:-4]), f)


if __name__ == '__main__':
    unittest.main()
