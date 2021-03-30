import unittest

from src.plataform import filters as f


class TestsFilters(unittest.TestCase):

    def test_candidate_sentences_all_empty(self):
        filters = f.filters()
        result = filters.candidate_sentences([['']], [frozenset([])])
        self.assertEqual(len(result), 0)

    def test_candidate_sentences_not_subset(self):
        filters = f.filters()
        result = filters.candidate_sentences([['Ameixa'], ['Ameixa'], ['Abacate']], [frozenset(['teste', 'unitário'])])
        self.assertEqual(len(result), 0)

    def test_candidate_sentences_subset(self):
        filters = f.filters()
        list_of_expected = ['Ameixa', 'muito', 'saborosa']

        result = filters.candidate_sentences([list_of_expected, ['Ameixa'], ['Abacate']], [frozenset(['saborosa'])])
        expected = [list_of_expected]

        self.assertEqual(len(result), 1)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
