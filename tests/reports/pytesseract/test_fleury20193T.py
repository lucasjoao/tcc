import unittest
from src import manager as m
from src.helper import result_helper as rh
from data import data as data


class TestsFleury20193T(unittest.TestCase):

    filename = None
    manager_pytesseract = None

    @classmethod
    def setUpClass(cls):
        cls.filename = 'fleury_2019_3T.pdf'
        cls.manager_pytesseract = m.manager([cls.filename], 'pytesseract')

    @classmethod
    def tearDownClass(cls):
        cls.filename = None
        cls.manager_pytesseract = None

    def test_lucro_liquido_monetary(self):
        result = self.manager_pytesseract.run_lucro_liquido_monetary()[self.filename]

        self.assertEqual(len(result), 0, 'lucro líquido (R$): tamanho resultado')

    def test_lucro_liquido_number(self):
        lucro_liquido_number_pytesseract = self.manager_pytesseract.run_lucro_liquido_number()
        result_pytesseract = lucro_liquido_number_pytesseract[self.filename]
        numbers_from_result_pytesseract = rh.result_helper.get_numbers_as_list(result_pytesseract)

        self.assertEqual(len(result_pytesseract), 1,
                         'lucro líquido (número após conjunto de busca): tamanho resultado (pytesseract)')
        self.assertIn(data.LUCRO_LIQUIDO[self.filename], numbers_from_result_pytesseract,
                      'lucro líquido (número após conjunto de busca): valor (pytesseract)')

    def test_patrimonio_liquido_monetary(self):
        result = self.manager_pytesseract.run_patrimonio_liquido_monetary()[self.filename]

        self.assertEqual(len(result), 0, 'patrimônio líquido (R$): tamanho resultado')

    def test_patrimonio_liquido_number(self):
        result = self.manager_pytesseract.run_patrimonio_liquido_number()[self.filename]
        number_from_result = rh.result_helper.get_numbers_as_list(result)

        self.assertEqual(len(result), 3, 'patrimônio líquido (número após conjunto de busca): tamanho resultado')
        self.assertIn(data.PATRIMONIO_LIQUIDO[self.filename], number_from_result,
                      'patrimônio líquido (número após conjunto de busca): valor')

    def test_roe_monetary(self):
        result = self.manager_pytesseract.run_roe_monetary()[self.filename]

        self.assertEqual(len(result), 0, 'ROE (R$): tamanho resultado')

    def test_roe_number(self):
        result = self.manager_pytesseract.run_roe_number()[self.filename]

        self.assertEqual(len(result), 0, 'ROE (número após conjunto de busca): tamanho resultado')

    def test_roe_calculate(self):
        result = self.manager_pytesseract.run_calculate_roe()[self.filename]

        self.assertEqual(len(result), 3, 'ROE por cálculo: tamanho resultado')
        self.assertIn(data.ROE[self.filename], result, 'ROE por cálculo: valor')


if __name__ == '__main__':
    unittest.main()
