
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
        self.fail("TODO: Write power unit test")

    def test_factorial(self):
        self.fail("TODO: Write factorial unit test")

    def test_fibonacci(self):
        self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
