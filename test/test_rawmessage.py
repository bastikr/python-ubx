import unittest

import ubx


class TestRawMessage(unittest.TestCase):
    def test_length(self):
        msg_class = b"\x01"
        msg_id = b"\x02"
        msg = ubx.RawMessage(msg_class, msg_id, b"")
        self.assertEqual(len(msg), 0)
        msg = ubx.RawMessage(msg_class, msg_id, b"\x02\xf1")
        self.assertEqual(len(msg), 2)

    def test_lengthbytes(self):
        msg_class = b"\x01"
        msg_id = b"\x02"
        msg = ubx.RawMessage(msg_class, msg_id, b"")
        self.assertEqual(msg.lengthbytes, b"\x00\x00")
        msg = ubx.RawMessage(msg_class, msg_id, b"\x02\xf1")
        self.assertEqual(msg.lengthbytes, b"\x02\x00")
