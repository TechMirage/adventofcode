import unittest
from PasswordCheckerTwo import PasswordChecker

class TestingClass(unittest.TestCase):

    def setUp(self):
        self.checker = PasswordChecker()

    def test_decode_db(self):
        x, y, z, w = self.checker.decode_db("1-3 a: abcde")
        self.assertEqual(x, 1)
        self.assertEqual(y, 3)
        self.assertEqual(z, "a")
        self.assertEqual(w, "abcde")

    def test_call(self):
        entries = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc", "1-2 b: bbbf"]
        self.checker.valid_passwords = 0
        for entry in entries:
            self.checker(entry)
        self.assertEqual(self.checker.valid_passwords, 1)

    def test_contains_target(self):
        x = self.checker.contains_target(1, 3, 'a', 'abcde')
        self.assertEqual(x, True)
        y = self.checker.contains_target(2, 9, 'c', 'ccccccccc')
        self.assertEqual(y, False)


if __name__ == '__main__':
    unittest.main()
