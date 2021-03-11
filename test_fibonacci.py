import unittest

import sys
from fibonacci import factorial, fibonacci

class TestFibbonaci(unittest.TestCase):
    def test_fibCorrect1(self):
        self.assertEqual(fibonacci(1), 1)
    def test_fibCorrect2(self):
        self.assertEqual(fibonacci(4), 3)
    def test_fibNegative(self):
        self.assertEqual(fibonacci(-13), None)
    def test_fibString(self):
        self.assertEqual(fibonacci("stringInput"), None)


    def test_facCorrect1(self):
        self.assertEqual(factorial(0), 1)
    def test_facCorrect2(self):
        self.assertEqual(factorial(4), 24)
    def test_facNegative(self):
        self.assertEqual(factorial(-13), None)
    def test_facString(self):
        self.assertEqual(factorial("stringInput"), None)

if __name__ == '__main__':
    unittest.main()
