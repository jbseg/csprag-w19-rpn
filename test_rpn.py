import unittest

import rpn

def run_error():
    result = rpn.calculate("1 1 1 +")

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
    def test_errors(self):
        self.assertRaises(TypeError, run_error)
        

def main():
    test = TestBasics()
    test.test_add()
    test.test_subtract()
    test.test_multiply()
    test.test_divide()
    test.test_expo() 
    test.test_errors()

if __name__ == '__main__':
    unittest.main()