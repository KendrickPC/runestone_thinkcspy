import unittest
import calculate


class TestCalculate(unittest.TestCase):

    def test_add(self):
        # https://docs.python.org/3/library/unittest.html
        result = calculate.add(10, 5)
        self.assertEqual(result, 15)     


if __name__ == '__main__':
    unittest.main()
