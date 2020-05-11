# -*- coding: utf-8 -*-
import unittest
from src import searcher as searcher


class TestsSearcher(unittest.TestCase):

    def setUp(self):
        self.searcher = searcher.Searcher(['ROE', 'retorno on equity'])

    def test_roe_found(self):
        result = self.searcher.run('empresa x teve o ROE 1.25%')
        self.assertEqual(result, '1.25%')

    def test_roe_not_found(self):
        result = self.searcher.run('empresa x não divulga o indicador que eu procuro explicitamente')
        self.assertEqual(result, 'Nada encontrado!')


if __name__ == '__main__':
    unittest.main()
