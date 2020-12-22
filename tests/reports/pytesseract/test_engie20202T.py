import unittest
from src import manager as m
from src.helper import result_helper as rh
from data import data as data


class TestsEngie20202T(unittest.TestCase):

    filename = None
    manager_pypdf2 = None
    manager_pytesseract = None

    @classmethod
    def setUpClass(cls):
        cls.filename = 'engie_2020_2T.pdf'
        cls.manager_pypdf2 = m.manager([cls.filename], 'pypdf2')
        cls.manager_pytesseract = m.manager([cls.filename], 'pytesseract')

    @classmethod
    def tearDownClass(cls):
        cls.filename = None
        cls.manager_pypdf2 = None
        cls.manager_pytesseract = None

    def test_lucro_liquido_monetary(self):
        lucro_liquido_monetary_pypdf2 = self.manager_pypdf2.run_lucro_liquido_monetary()
        lucro_liquido_monetary_pytesseract = self.manager_pytesseract.run_lucro_liquido_monetary()
        result_pypdf2 = lucro_liquido_monetary_pypdf2[self.filename]
        result_pytesseract = lucro_liquido_monetary_pytesseract[self.filename]
        numbers_from_result_pypdf2 = rh.result_helper.get_numbers_as_list(result_pypdf2)
        numbers_from_result_pytesseract = rh.result_helper.get_numbers_as_list(result_pytesseract)

        self.assertEqual(len(result_pypdf2), 6, 'lucro líquido (R$): tamanho resultado (pypdf2)')
        self.assertIn(data.LUCRO_LIQUIDO[self.filename], numbers_from_result_pypdf2, 'lucro líquido (R$): valor (pypdf2)')
        self.assertEqual(len(result_pytesseract), 4, 'lucro líquido (R$): tamanho resultado (pytesseract)')
        self.assertIn(data.LUCRO_LIQUIDO[self.filename],
                      numbers_from_result_pytesseract,
                      'lucro líquido (R$): valor (pytesseract)')

    def test_lucro_liquido_number(self):
        lucro_liquido_number_pypdf2 = self.manager_pypdf2.run_lucro_liquido_number()
        lucro_liquido_number_pytesseract = self.manager_pytesseract.run_lucro_liquido_number()
        result_pypdf2 = lucro_liquido_number_pypdf2[self.filename]
        result_pytesseract = lucro_liquido_number_pytesseract[self.filename]

        self.assertEqual(len(result_pypdf2), 0, 'lucro líquido (número após conjunto de busca): tamanho resultado')
        self.assertEqual(result_pypdf2, result_pytesseract, 'ambas libs trazem o mesmo resultado')

    def test_patrimonio_liquido_monetary(self):
        patrimonio_liquido_monetary = self.manager_pypdf2.run_patrimonio_liquido_monetary()
        result = patrimonio_liquido_monetary[self.filename]

        self.assertEqual(len(result), 0, 'patrimônio líquido (R$): tamanho resultado')
        self.assertEqual(result,
                         self.manager_pytesseract.run_patrimonio_liquido_monetary()[self.filename],
                         'ambas libs trazem o mesmo resultado')

    def test_patrimonio_liquido_number(self):
        patrimonio_liquido_number_pypdf2 = self.manager_pypdf2.run_patrimonio_liquido_number()
        patrimonio_liquido_number_pytesseract = self.manager_pytesseract.run_patrimonio_liquido_number()
        result_pypdf2 = patrimonio_liquido_number_pypdf2[self.filename]
        result_pytesseract = patrimonio_liquido_number_pytesseract[self.filename]

        self.assertEqual(len(result_pypdf2), 0,
                         'patrimônio líquido (número após conjunto de busca): tamanho resultado (pypdf2)')
        self.assertEqual(len(result_pytesseract), 1,
                         'patrimônio líquido (número após conjunto de busca): tamanho resultado (pytesseract)')
        self.assertEqual(result_pytesseract[0]['number'], data.PATRIMONIO_LIQUIDO[self.filename],
                         'patrimônio líquido (número após conjunto de busca): valor (pytesseract)')

    def test_roe_monetary(self):
        roe_monetary = self.manager_pypdf2.run_roe_monetary()
        result = roe_monetary[self.filename]

        self.assertEqual(len(result), 0, 'ROE (R$): tamanho resultado')
        self.assertEqual(result, self.manager_pytesseract.run_roe_monetary()[self.filename],
                         'ambas libs trazem o mesmo resultado')

    def test_roe_number(self):
        roe_number = self.manager_pypdf2.run_roe_number()
        result = roe_number[self.filename]

        self.assertEqual(len(result), 0, 'ROE (número após conjunto de busca): tamanho resultado')
        self.assertEqual(result, self.manager_pytesseract.run_roe_number()[self.filename],
                         'ambas libs trazem o mesmo resultado')

    def test_roe_calculate(self):
        roe_calculate_pypdf2 = self.manager_pypdf2.run_calculate_roe()
        roe_calculate_pytesseract = self.manager_pytesseract.run_calculate_roe()
        result_pypdf2 = roe_calculate_pypdf2[self.filename]
        result_pytesseract = roe_calculate_pytesseract[self.filename]

        self.assertEqual(len(result_pypdf2), 0, 'ROE por cálculo: tamanho resultado (pypdf2)')
        self.assertEqual(len(result_pytesseract), 4, 'ROE por cálculo: tamanho resultado (pytesseract)')
        self.assertIn(data.ROE[self.filename], result_pytesseract, 'ROE por cálculo: valor (pytesseract)')


if __name__ == '__main__':
    unittest.main()
