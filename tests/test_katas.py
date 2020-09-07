
__author__ = 'Gabby, collabs: Shanquel and Sondos'

import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(2, 1), 3)
        self.assertEqual(katas.add(-5, 3), -2)
        self.assertEqual(katas.add(105, 15), 120)

    def test_multiply(self):
        self.assertEqual(katas.multiply(5, 5), 25)
        self.assertEqual(katas.multiply(10, 10), 100)
        self.assertEqual(katas.multiply(25, 10), 250)

    def test_power(self):
        self.assertEqual(katas.power(2, 0), 1)
        self.assertEqual(katas.power(5, 3), 125)
        self.assertEqual(katas.power(8, 1), 8)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)
        self.assertEqual(katas.factorial(4), 24)
        self.assertEqual(katas.factorial(3), 6)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(0), -1)
        self.assertEqual(katas.fibonacci(4), 2)
        self.assertEqual(katas.fibonacci(9), 21)


if __name__ == '__main__':
    unittest.main()
