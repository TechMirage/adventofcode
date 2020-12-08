import unittest
import part2

class TestingClass(unittest.TestCase):

    def setUp(self):
        self.test_data='nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6'
        self.test_data_correct='nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\nnop -4\nacc +6'

    def tearDown(self):
        pass

    def test_run_code(self):
        code = self.test_data_correct.split('\n')
        tmp = part2.run_code(code)
        self.assertEqual(tmp, 8)

    def test_process(self):
        tmp = part2.process(self.test_data)
        self.assertEqual(tmp, 8)

if __name__ == '__main__':
    unittest.main()
