import unittest
from number import Number

class TestNumberMethods(unittest.TestCase):

    def test_parsing(self):
        self.assertEqual(Number("123456"), Number(123456))
        self.assertEqual(Number("-123456"), Number(-123456))
        self.assertEqual(Number([3456, 12]), Number(123456))

    def test_string(self):
        self.assertEqual(str(Number(123)), "123")

    def test_equality(self):
        self.assertNotEqual(Number(123456), Number(654321))
        self.assertEqual(Number("123456"), Number(123456))
        self.assertEqual(Number("inf"), Number("inf"))

    def test_order_with_finite_numbers(self):
        self.assertLess(Number(123456), Number(654321))
        self.assertLessEqual(Number(123456), Number(123456))
        self.assertLess(Number(-654321), Number(123456))
        self.assertGreater(Number(654321), Number(123456))
        self.assertGreaterEqual(Number(123456), Number(123456))
        self.assertGreater(Number(123456), Number(-654321))

    def test_order_with_infinity(self):
        self.assertLess(Number(123456), Number("inf"))
        self.assertLessEqual(Number(123456), Number("Inf"))
        self.assertGreater(Number("inf"), Number(123456))
        self.assertGreaterEqual(Number("inf"), Number(123456))
        self.assertLess(Number("-inf"), Number("inf"))
        self.assertGreater(Number("inf"), Number("-inf"))

    def test_multiplcation(self):
        self.assertEqual(Number(123) * Number(456), Number(123 * 456))
        self.assertEqual(Number(123) * Number("inf"), Number("inf"))
        self.assertEqual(Number(123) * Number("-inf"), Number("-inf"))

    def test_addition(self):
        self.assertEqual(Number(123) + Number(456), Number(123 + 456))
        self.assertEqual(Number(123) + Number("inf"), Number("inf"))
        self.assertEqual(Number("inf") + Number(123), Number("inf"))
        self.assertEqual(Number(123) + Number("-inf"), Number("-inf"))
        self.assertEqual(Number("-inf") + Number(123), Number("-inf"))
        self.assertRaises(ArithmeticError, lambda: Number("-inf") + Number("inf"))

    def test_subtraction(self):
        self.assertEqual(Number(123) - Number(456), Number(123 - 456))
        self.assertEqual(Number(123) - Number(123), Number(0))
        self.assertEqual(Number("inf") - Number(123), Number("inf"))
        self.assertEqual(Number(123) - Number("inf"), Number("-inf"))
        self.assertEqual(Number("-inf") - Number(123), Number("-inf"))
        self.assertEqual(Number(123) - Number("-inf"), Number("inf"))
        self.assertRaises(ArithmeticError, lambda: Number("inf") - Number("inf"))

    def test_quotient(self):
        self.assertEqual(Number(654) // Number(321), Number(654 // 321))
        self.assertEqual(Number(123) // Number(456), Number(123 // 456))
        self.assertEqual(Number(123) // Number("inf"), Number(0))
        self.assertEqual(Number(123) // Number("-inf"), Number(0))
        self.assertEqual(Number("inf") // Number(123), Number("inf"))
        self.assertEqual(Number("-inf") // Number(123), Number("-inf"))
        self.assertRaises(ArithmeticError, lambda: Number("inf") // Number("inf"))
        self.assertRaises(ArithmeticError, lambda: Number(123) // Number(0))

    def test_remainder(self):
        self.assertEqual(Number(654) % Number(321), Number(654 % 321))
        self.assertEqual(Number(123) % Number(456), Number(123 % 456))
        self.assertEqual(Number(123) % Number("inf"), Number(123))
        self.assertEqual(Number(123) % Number("-inf"), Number(123))
        self.assertEqual(Number("inf") % Number(123), Number("inf"))
        self.assertEqual(Number("-inf") % Number(123), Number("-inf"))
        self.assertRaises(ArithmeticError, lambda: Number("inf") % Number("inf"))
        self.assertRaises(ArithmeticError, lambda: Number(123) % Number(0))

if __name__ == '__main__':
    unittest.main()