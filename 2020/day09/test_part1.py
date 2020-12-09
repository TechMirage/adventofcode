import unittest
import part1

class TestingClass(unittest.TestCase):

    def setUp(self):
        self.test_data="35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576"

    def tearDown(self):
        pass

    def test_process(self):
        ans = part1.process(self.test_data, preamble_size=5)
        self.assertEqual(ans, 127)


if __name__ == '__main__':
    unittest.main()
