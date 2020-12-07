import unittest
import part2

class TestingClass(unittest.TestCase):

    def setUp(self):
        self.test_data = "shiny gold bags contain 2 dark red bags.\ndark red bags contain 2 dark orange bags.\ndark orange bags contain 2 dark yellow bags.\ndark yellow bags contain 2 dark green bags.\ndark green bags contain 2 dark blue bags.\ndark blue bags contain 2 dark violet bags.\ndark violet bags contain no other bags."

    def tearDown(self):
        pass

    def test_process(self):
        ans = part2.process(self.test_data)
        self.assertEqual(ans, 126)

if __name__ == '__main__':
    unittest.main()
