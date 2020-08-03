# -*- coding: utf-8 -*-
import unittest
from src.indicator import roe_calculator as roe


class TestRoeCalculator(unittest.TestCase):

    def test_roe_found(self):
        roe_calculator = roe.RoeCalculator('weg possui um ROE 32% em 2022')
        result = roe_calculator.execute()
        self.assertEqual(result, '32%')

    def test_nothing_found(self):
        roe_calculator = roe.RoeCalculator('esse texto dummy não possui nenhuma info para o indicador')
        result = roe_calculator.execute()
        self.assertIsNone(result)

    def test_almost_nothing_found(self):
        roe_calculator = roe.RoeCalculator('esse texto dummy só possui o lucro líquido 2.00')
        result = roe_calculator.execute()
        self.assertIsNone(result)

    def test_calculation(self):
        roe_calculator = roe.RoeCalculator('esse texto possui lucro líquido 2.00 e patrimônio líquido 78.00')
        result = roe_calculator.execute()
        self.assertEqual(result, 2.56)

    # teste dado real para os mesmos itens anteriores


if __name__ == '__main__':
    unittest.main()
