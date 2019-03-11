import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_expo(self):
        result = rpn.calculate("6 2 ^")
        self.assertEqual(36, result)

def main():
    test = TestBasics()
    test.test_add()
    test.test_subtract()
    test.test_multiply()
    test.test_divide()
    test.test_expo() 

if __name__ == '__main__':
    unittest.main()