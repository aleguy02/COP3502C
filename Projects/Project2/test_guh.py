import unittest
from guh import encode_rle


class TestCountRuns(unittest.TestCase):
    def test_encode_rle1(self):
        self.assertEqual(encode_rle([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7]),
                         [2,4,15,1,15,1,5,1,1,8,1,7])

    def test_encode_rle2(self):
        self.assertEqual(encode_rle([1,2,3,4,1,2,3,4]),
                         [1,1,1,2,1,3,1,4,1,1,1,2,1,3,1,4])

    def test_encode_rle3(self):
        self.assertEqual(encode_rle([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),
                         [2,4,15,1,15,1,5,1])

    def test_encode_rle4(self):
        self.assertEqual(encode_rle([4,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),
                         [1,4,1,5,15,1,15,1,5,1])


if __name__ == '__main__':
    unittest.main()
