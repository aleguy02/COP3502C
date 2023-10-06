import unittest
from guh import count_runs


class TestCountRuns(unittest.TestCase):
    def test_count_runs1(self):
        self.assertEqual(count_runs([15, 15, 15, 4, 4, 4, 4, 4, 4]), 2)

    def test_count_runs2(self):
        self.assertEqual(count_runs([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7 ]), 6)

    def test_count_runs3(self):
        self.assertEqual(count_runs([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]), 25)


if __name__ == '__main__':
    unittest.main()
