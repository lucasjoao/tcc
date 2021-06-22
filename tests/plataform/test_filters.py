import unittest

from src.plataform import filters as f


class TestsFilters(unittest.TestCase):

    filters = None

    @classmethod
    def setUpClass(cls):
        cls.filters = f.filters()

    @classmethod
    def tearDownClass(cls):
        cls.filters = None

    def test_candidate_sentences_all_empty(self):
        result = self.filters.candidate_sentences([['']], [frozenset([])])
        self.assertEqual(len(result), 0)

    def test_candidate_sentences_not_subset(self):
        result = self.filters.candidate_sentences([['Ameixa'], ['Ameixa'], ['Abacate']], [frozenset(['teste', 'unitário'])])
        self.assertEqual(len(result), 0)

    def test_candidate_sentences_subset(self):
        list_of_expected = ['Ameixa', 'muito', 'saborosa']

        result = self.filters.candidate_sentences([list_of_expected, ['Ameixa'], ['Abacate']], [frozenset(['saborosa'])])
        expected = [list_of_expected]

        self.assertEqual(len(result), 1)
        self.assertEqual(expected, result)

    def test_is_searcher_words_in_sequence_all_empty(self):
        result = self.filters.is_searcher_words_in_sequence([[]], [['vazio']])
        self.assertEqual(len(result), 0)

    def test_is_searcher_words_in_sequence_empty_position(self):
        candidate_sentences = [['eu', 'gost', 'abacat', 'tard', '.'],
                               ['-', 'ach', 'bom', 'gost', 'abacax', 'barat', 'r', '$', '.'],
                               ['gost', 'tangerin', 'cust', 'r', '$', '.']]
        result = self.filters.is_searcher_words_in_sequence(candidate_sentences, [['avela']])
        self.assertEqual(len(result), 0)

    def test_is_searcher_words_in_sequence_is_hit_by_except(self):
        candidate_sentences = [['eu'],
                               ['-', 'ach', 'bom', 'gost', 'abacax', 'barat', 'r', '$', '.'],
                               ['gost', 'tangerin', 'cust', 'r', '$', '.']]
        result = self.filters.is_searcher_words_in_sequence(candidate_sentences, [['eu', 'abacat']])
        self.assertEqual(len(result), 0)

    def test_is_searcher_words_in_sequence_is_hit_false(self):
        candidate_sentences = [['eu', 'gost', 'abacat', 'tard', '.'],
                               ['-', 'ach', 'bom', 'gost', 'abacax', 'barat', 'r', '$', '.'],
                               ['gost', 'tangerin', 'cust', 'r', '$', '.']]
        result = self.filters.is_searcher_words_in_sequence(candidate_sentences, [['barat', 'abacat']])
        self.assertEqual(len(result), 0)

    def test_is_searcher_words_in_sequence_success(self):
        candidate_sentences = [['eu', 'gost', 'abacat', 'tard', '.'],
                               ['-', 'ach', 'bom', 'gost', 'abacax', 'barat', 'r', '$', '.'],
                               ['gost', 'tangerin', 'cust', 'r', '$', '.']]
        result = self.filters.is_searcher_words_in_sequence(candidate_sentences, [['gost', 'abacat']])

        self.assertEqual(len(result), 1)
        self.assertEqual(result, [('eu', 'gost', 'abacat', 'tard', '.')])


if __name__ == '__main__':
    unittest.main()
