import unittest
import part1 as code

class TestingClass(unittest.TestCase):

    def setUp(self):
        self.test_data = "F10\nN3\nF7\nR90\nF11"

    def tearDown(self):
        pass

    def test_process(self):
        ans = code.process(self.test_data)
        self.assertEqual(ans, 25)


if __name__ == '__main__':
    unittest.main()
