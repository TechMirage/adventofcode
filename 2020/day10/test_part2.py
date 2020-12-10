import unittest
import part2

class TestingClass(unittest.TestCase):

    def setUp(self):
        self.test_data_1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        self.test_data_2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 
                            23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 
                            8, 17, 7, 9, 4, 2, 34, 10, 3]

    def tearDown(self):
        pass

    def test_process(self):
        ans1 = part2.process(self.test_data_1)
        ans2 = part2.process(self.test_data_2)
        self.assertEqual(ans1, 8)
        self.assertEqual(ans2, 19208)

if __name__ == '__main__':
    unittest.main()
