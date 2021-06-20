import unittest
from src.plataform import searcher as s


class TestsSearcher(unittest.TestCase):

    searcher = None

    @classmethod
    def setUpClass(cls):
        cls.searcher = s.searcher()

    @classmethod
    def tearDownClass(cls):
        cls.searcher = None

    def test_monetary_value_empty_candidate_sentences(self):
        result = self.searcher.monetary_value([])
        self.assertEqual(len(result), 0)

    def test_monetary_value_empty_sentences(self):
        result = self.searcher.monetary_value([[], [], []])
        self.assertEqual(len(result), 0)

    def test_monetary_value_without_numbers(self):
        candidate_sentences = [['eu', 'gost', 'abacat', 'tard', '.'],
                               ['-', 'ach', 'bom', 'gost', 'abacax', 'barat', 'r', '$', '.'],
                               ['gost', 'tangerin', 'cust', 'r', '$', '.']]
        result = self.searcher.monetary_value(candidate_sentences)
        self.assertEqual(len(result), 0)

    def test_monetary_value_numbers_with_invalid_positions(self):
        candidate_sentences = [['3', '-', 'ach', 'bom', 'gost', 'abacax']]
        result = self.searcher.monetary_value(candidate_sentences)
        self.assertEqual(len(result), 0)

    def test_monetary_value_number_not_monetary(self):
        candidate_sentences = [['eu', 'gost', 'abacat', '6', 'tard', '.'],
                               ['3', '-', 'ach', 'bom', 'gost', 'abacax', 'barat', '2.50', '.'],
                               ['gost', 'tangerin', 'cust', '1.00', '.']]
        result = self.searcher.monetary_value(candidate_sentences)
        self.assertEqual(len(result), 0)

    def test_monetary_value_success(self):
        candidate_sentences = [['eu', 'gost', 'abacat', '6', 'tard', '.'],
                               ['3', '-', 'ach', 'bom', 'gost', 'abacax', 'barat', 'r', '$', '2.50', '.'],
                               ['gost', 'tangerin', 'cust', 'r', '$', '1.00', '.']]
        result = self.searcher.monetary_value(candidate_sentences)
        self.assertEqual(len(result), 2)
        self.assertEqual([{'number': 2.5, 'possible_size': '.'}, {'number': 1.0, 'possible_size': '.'}], result)


if __name__ == '__main__':
    unittest.main()
