import unittest

from ubx.descriptions import mon_hw


class TestDescriptions(unittest.TestCase):
    def test_parse(self):
        print(mon_hw.description)

if __name__ == '__main__':
    unittest.main()
