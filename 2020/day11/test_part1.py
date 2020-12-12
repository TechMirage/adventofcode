import unittest
import part1 as code 

class TestingClass(unittest.TestCase):

    def setUp(self):
        self.test_data = "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL"

    def tearDown(self):
        pass

    def test_process(self):
        ans = code.process(self.test_data)
        self.assertEqual(ans, 37)

if __name__ == '__main__':
    unittest.main()
