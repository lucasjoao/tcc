import unittest
import math
from src.helper import number_helper as nh


class TestsNumberHelper(unittest.TestCase):

    def test_without_dot(self):
        is_number, number = nh.number_helper.is_number('100')

        self.assertTrue(is_number)
        self.assertEqual(number, 100)

    def test_one_dot_and_one_comma_decimal(self):
        is_number, number = nh.number_helper.is_number('1.234,50')

        self.assertTrue(is_number)
        self.assertEqual(number, 1234.50)

    def test_more_than_one_comma(self):
        is_number, number = nh.number_helper.is_number('1,234,50')

        self.assertFalse(is_number)
        self.assertTrue(math.isnan(number))

    def test_one_dot_two_decimals(self):
        is_number, number = nh.number_helper.is_number('1234.12')

        self.assertTrue(is_number)
        self.assertEqual(number, 1234.12)

    def test_one_dot_one_decimal(self):
        is_number, number = nh.number_helper.is_number('1234.0')

        self.assertTrue(is_number)
        self.assertEqual(number, 1234.0)

    def test_word_nan(self):
        is_number, number = nh.number_helper.is_number('abacate')

        self.assertFalse(is_number)
        self.assertTrue(math.isnan(number))

    def test_more_one_dot(self):
        is_number, number = nh.number_helper.is_number('1.234.567')

        self.assertTrue(is_number)
        self.assertEqual(number, 1234567.0)

    def test_more_one_dot_and_decimal(self):
        is_number, number = nh.number_helper.is_number('1.234.567.89')

        self.assertTrue(is_number)
        self.assertEqual(number, 1234567.89)

    def test_more_one_dot_and_decimal_nan(self):
        is_number, number = nh.number_helper.is_number('1.234.567.890000')

        self.assertFalse(is_number)
        self.assertTrue(math.isnan(number))

    def test_dot_and_comma_one_decimal(self):
        is_number, number = nh.number_helper.is_number('2.587,6')

        self.assertTrue(is_number)
        self.assertEqual(number, 2587.6)

    def test_dot_and_comma_without_decimal(self):
        is_number, number = nh.number_helper.is_number('2.587,')

        self.assertFalse(is_number)
        self.assertTrue(math.isnan(number))


if __name__ == '__main__':
    unittest.main()
