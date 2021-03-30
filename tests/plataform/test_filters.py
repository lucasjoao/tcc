import unittest

from src.plataform import filters as f


class TestsFilters(unittest.TestCase):

    def test_candidate_sentences_all_empty(self):
        filters = f.filters()
        result = filters.candidate_sentences([''], [frozenset([])])
        self.assertEqual(len(result), 0)

    def test_candidate_sentences_not_subset(self):
        filters = f.filters()
        result = filters.candidate_sentences(['Ameixa', 'Ameixa', 'Abacate'], [frozenset(['teste', 'unitário'])])
        self.assertEqual(len(result), 0)

    # NEED FIX
    def test_candidate_sentences_subset(self):
        filters = f.filters()
        result = filters.candidate_sentences(['Ameixa muito saborosa', 'Ameixa', 'Abacate'], [frozenset(['saborosa'])])
        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()
