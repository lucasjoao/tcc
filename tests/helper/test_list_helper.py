import unittest

from src.helper import list_helper as lh


class TestsListHelper(unittest.TestCase):

    def test_remove_duplicates_lists_ok(self):
        list_of_lists = [['Abacate', 'Abacate', 'Granola'], ['Abacate', 'Granola'], ['Abacate', 'Granola']]
        result = lh.list_helper.remove_duplicates_list_of_lists(list_of_lists)

        self.assertEqual(len(result), 2)
        self.assertIn(('Abacate', 'Abacate', 'Granola'), result)
        self.assertIn(('Abacate', 'Granola'), result)

    def test_remove_duplicates_lists_not_remove(self):
        list_of_lists = [['Abacate', 'Abacate', 'Granola'], ['Abacate', 'Granola']]
        result = lh.list_helper.remove_duplicates_list_of_lists(list_of_lists)

        self.assertEqual(len(result), len(list_of_lists))
        self.assertIn(('Abacate', 'Abacate', 'Granola'), result)
        self.assertIn(('Abacate', 'Granola'), result)

    def test_remove_duplicates_list_empty(self):
        result = lh.list_helper.remove_duplicates_list_of_lists([])
        self.assertEqual(len(result), 0)

    def test_remove_duplicates_dict_ok(self):
        list_of_dicts = [{'key0': 1}, {'key1': 2, 'key2': 3}, {'key0': 1}]
        result = lh.list_helper.remove_duplicates_list_of_dicts(list_of_dicts)

        self.assertEqual(len(result), 2)
        self.assertIn({'key0': 1}, result)
        self.assertIn({'key1': 2, 'key2': 3}, result)

    def test_remove_duplicates_dict_not_remove(self):
        list_of_dicts = [{'key0': 1}, {'key1': 2, 'key2': 3}]
        result = lh.list_helper.remove_duplicates_list_of_dicts(list_of_dicts)

        self.assertEqual(len(result), len(list_of_dicts))
        self.assertIn({'key0': 1}, result)
        self.assertIn({'key1': 2, 'key2': 3}, result)

    def test_remove_duplicates_dict_empty(self):
        result = lh.list_helper.remove_duplicates_list_of_dicts([])
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
