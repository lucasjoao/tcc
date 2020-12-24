import unittest
from src import manager as m
from src.helper import result_helper as rh
from data import data as data


class TestsEngie20202T(unittest.TestCase):

    filename = None
    manager_pytesseract = None

    @classmethod
    def setUpClass(cls):
        cls.filename = 'engie_2020_2T.pdf'
        cls.manager_pytesseract = m.manager([cls.filename], 'pytesseract')

    @classmethod
    def tearDownClass(cls):
        cls.filename = None
        cls.manager_pytesseract = None

    def test_lucro_liquido_monetary(self):
        lucro_liquido_monetary_pytesseract = self.manager_pytesseract.run_lucro_liquido_monetary()
        result_pytesseract = lucro_liquido_monetary_pytesseract[self.filename]
        numbers_from_result_pytesseract = rh.result_helper.get_numbers_as_list(result_pytesseract)

        self.assertEqual(len(result_pytesseract), 5, 'lucro líquido (R$): tamanho resultado (pytesseract)')
        self.assertIn(data.LUCRO_LIQUIDO[self.filename],
                      numbers_from_result_pytesseract,
                      'lucro líquido (R$): valor (pytesseract)')

    def test_lucro_liquido_number(self):
        lucro_liquido_number_pytesseract = self.manager_pytesseract.run_lucro_liquido_number()
        result_pytesseract = lucro_liquido_number_pytesseract[self.filename]

        self.assertEqual(len(result_pytesseract), 0, 'lucro líquido (número após conjunto de busca): tamanho resultado')

    def test_patrimonio_liquido_monetary(self):
        result = self.manager_pytesseract.run_patrimonio_liquido_monetary()[self.filename]

        self.assertEqual(len(result), 0, 'patrimônio líquido (R$): tamanho resultado')

    def test_patrimonio_liquido_number(self):
        patrimonio_liquido_number_pytesseract = self.manager_pytesseract.run_patrimonio_liquido_number()
        result_pytesseract = patrimonio_liquido_number_pytesseract[self.filename]

        self.assertEqual(len(result_pytesseract), 1,
                         'patrimônio líquido (número após conjunto de busca): tamanho resultado (pytesseract)')
        self.assertEqual(result_pytesseract[0]['number'], data.PATRIMONIO_LIQUIDO[self.filename],
                         'patrimônio líquido (número após conjunto de busca): valor (pytesseract)')

    def test_roe_monetary(self):
        result = self.manager_pytesseract.run_roe_monetary()[self.filename]

        self.assertEqual(len(result), 0, 'ROE (R$): tamanho resultado')

    def test_roe_number(self):
        result = self.manager_pytesseract.run_roe_number()[self.filename]

        self.assertEqual(len(result), 0, 'ROE (número após conjunto de busca): tamanho resultado')

    def test_roe_calculate(self):
        roe_calculate_pytesseract = self.manager_pytesseract.run_calculate_roe()
        result_pytesseract = roe_calculate_pytesseract[self.filename]

        self.assertEqual(len(result_pytesseract), 5, 'ROE por cálculo: tamanho resultado (pytesseract)')
        self.assertIn(data.ROE[self.filename], result_pytesseract, 'ROE por cálculo: valor (pytesseract)')


if __name__ == '__main__':
    unittest.main()
