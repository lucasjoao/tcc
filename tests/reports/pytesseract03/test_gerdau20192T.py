import unittest
from src import manager as m
from src.helper import result_helper as rh
from data import data as data


class TestsGerdau20192T(unittest.TestCase):

    filename = None
    manager_pytesseract = None

    @classmethod
    def setUpClass(cls):
        cls.filename = 'gerdau_2019_2T.pdf'
        cls.manager_pytesseract = m.manager([cls.filename], 'pytesseract', '--psm 5')

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
        self.assertNotIn(data.LUCRO_LIQUIDO[self.filename], numbers_from_result_pytesseract,
                         'lucro líquido (número após conjunto de busca): valor (pytesseract)')

    def test_patrimonio_liquido_monetary(self):
        result = self.manager_pytesseract.run_patrimonio_liquido_monetary()[self.filename]

        self.assertEqual(len(result), 0, 'patrimônio líquido (R$): tamanho resultado')

    def test_patrimonio_liquido_number(self):
        patrimonio_liquido_number_pytesseract = self.manager_pytesseract.run_patrimonio_liquido_number()
        result_pytesseract = patrimonio_liquido_number_pytesseract[self.filename]

        self.assertEqual(len(result_pytesseract), 0,
                         'patrimônio líquido (número após conjunto de busca): tamanho resultado (pytesseract)')

    def test_roe_monetary(self):
        result = self.manager_pytesseract.run_roe_monetary()[self.filename]

        self.assertEqual(len(result), 0, 'ROE (R$): tamanho resultado')

    def test_roe_number(self):
        result = self.manager_pytesseract.run_roe_number()[self.filename]

        self.assertEqual(len(result), 0, 'ROE (número após conjunto de busca): tamanho resultado')

    def test_roe_calculate(self):
        calculate_roe_pytesseract = self.manager_pytesseract.run_calculate_roe()
        result_pytesseract = calculate_roe_pytesseract[self.filename]

        self.assertEqual(len(result_pytesseract), 0, 'ROE por cálculo: tamanho resultado (pytesseract)')


if __name__ == '__main__':
    unittest.main()
