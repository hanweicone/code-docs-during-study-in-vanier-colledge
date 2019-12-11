import unittest
import sys
print(sys.path)
# import function from another project
sys.path.append('C:/PycharmProjects/testUnit/testFunction')  # append module path
from testFunction import multi  # or import testFunction


class TestFunction1(unittest.TestCase):
    def test_numbers_2_4(self):
        self.assertEqual(multi(2, 4), 8)

    def test_numbers_3_6(self):
        self.assertEqual(multi(3, 6), 18)


class TestFunction2(unittest.TestCase):
    def test_numbers_2_5(self):
        self.assertEqual(multi(2, 5), 10)


if __name__ == '__main__':
    unittest.main()
