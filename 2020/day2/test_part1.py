import unittest
from PasswordChecker import PasswordChecker

class TestingClass(unittest.TestCase):

    def setUp(self):
        self.checker = PasswordChecker()

    def test_decode_db(self):
        x, y, z, w = self.checker.decode_db("1-3 a: abcde")
        self.assertEqual(x, 1)
        self.assertEqual(y, 3)
        self.assertEqual(z, "a")
        self.assertEqual(w, "abcde")

    def test_how_many_times(self):
        x = self.checker.how_many_times('b', 'abcde')
        self.assertEqual(x, 1)
        y = self.checker.how_many_times('c', 'ccccccc')
        self.assertEqual(y, 7)

    def test_call(self):
        entries = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc", "1-2 b: bbbf"]
        self.checker.valid_passwords = 0
        for entry in entries:
            self.checker(entry)
        self.assertEqual(self.checker.valid_passwords, 2)


if __name__ == '__main__':
    unittest.main()
