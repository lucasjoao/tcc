import unittest
from src.helper import result_helper as rh


class TestsResultHelper(unittest.TestCase):

    def test_create_result_item_with_undefined(self):
        result = rh.result_helper.create_result_item(25, '10')

        expected = {'number': 25, 'possible_size': 'undefined'}

        self.assertEqual(result, expected)

    def test_create_result_item_without_undefined(self):
        result = rh.result_helper.create_result_item(25, 'milhões')

        expected = {'number': 25, 'possible_size': 'milhões'}

        self.assertEqual(result, expected)

    def test_clean_search_result_success(self):
        test_input = [{'number': 10, 'possible_size': 'undefined'},
                      {'number': 30, 'possible_size': 40},
                      {'possible_size': 50}]
        result = rh.result_helper.clean_search_result(test_input)

        expected = [{'number': 30, 'possible_size': 40}, {'possible_size': 50}]
        self.assertEqual(result, expected)

    def test_clean_search_result_without_undefined(self):
        test_input = [{'number': 10, 'possible_size': 20},
                      {'number': 30, 'possible_size': 40},
                      {'possible_size': 50}]
        result = rh.result_helper.clean_search_result(test_input)

        expected = [{'number': 10, 'possible_size': 20},
                    {'number': 30, 'possible_size': 40},
                    {'possible_size': 50}]
        self.assertEqual(result, expected)

    def test_clean_search_result_empty(self):
        result = rh.result_helper.clean_search_result([])

        expected = []
        self.assertEqual(result, expected)

    def test_get_numbers_as_list_witht_number_key(self):
        test_input = [{'number': 10, 'other_key': 20}, {'number': 30, 'other_key': 40}, {'other_key': 50}]
        result = rh.result_helper.get_numbers_as_list(test_input)

        expected = [10, 30]
        self.assertEqual(result, expected)

    def test_get_numbers_as_list_without_number_key(self):
        test_input = [{'numb': 10, 'other_key': 20}, {'other_key': 40}, {'other_key': 50}]
        result = rh.result_helper.get_numbers_as_list(test_input)

        expected = []
        self.assertEqual(result, expected)

    def test_get_numbers_as_list_empty(self):
        result = rh.result_helper.get_numbers_as_list([])

        expected = []
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
