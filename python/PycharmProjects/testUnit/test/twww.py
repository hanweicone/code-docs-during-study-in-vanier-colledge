import unittest
import sys

print(sys.path)
# import function from another project
sys.path.append('C:/PycharmProjects/testUnit/testFunction')  # append module path
from testFunction import multi  # or import testFunction


class TestFunction3(unittest.TestCase):
    def test_numbers_7_8(self):
        self.assertEqual(multi(7, 8), 56)


# if do not use main,run multiple file will cause error
if __name__ == '__main__':
    unittest.main()
