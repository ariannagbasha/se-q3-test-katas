import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        add = self.module.add
        self.assertEqual(add(2, 1), 3)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(105,15), 130)

    def test_multiply(self):
        self.fail("TODO: Write multiply unit test")

    def test_power(self):
        self.fail("TODO: Write power unit test")

    def test_factorial(self):
        self.fail("TODO: Write factorial unit test")

    def test_fibonacci(self):
        self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
