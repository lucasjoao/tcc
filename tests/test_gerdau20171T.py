import unittest
from src import manager as m
from data import data as data


class TestsGerdau20171T(unittest.TestCase):

    filename = None
    manager_pypdf2 = None
    manager_pytesseract = None

    @classmethod
    def setUpClass(cls):
        cls.filename = 'gerdau_2017_1T.pdf'
        cls.manager_pypdf2 = m.manager([cls.filename], 'pypdf2')
        cls.manager_pytesseract = m.manager([cls.filename], 'pytesseract')

    @classmethod
    def tearDownClass(cls):
        cls.filename = None
        cls.manager_pypdf2 = None
        cls.manager_pytesseract = None

    def test_lucro_liquido_monetary(self):
        lucro_liquido_monetary = self.manager_pypdf2.run_lucro_liquido_monetary()
        result = lucro_liquido_monetary[self.filename]

        self.assertEqual(len(result), 0, 'lucro líquido (R$): tamanho resultado')
        self.assertEqual(result,
                         self.manager_pytesseract.run_lucro_liquido_monetary()[self.filename],
                         'ambas libs trazem o mesmo resultado')

    def test_lucro_liquido_number(self):
        lucro_liquido_number = self.manager_pypdf2.run_lucro_liquido_number()
        result = lucro_liquido_number[self.filename]

        self.assertEqual(len(result), 1, 'lucro líquido (número após conjunto de busca): tamanho resultado')
        self.assertEqual(result[0]['number'], data.LUCRO_LIQUIDO[self.filename],
                         'lucro líquido (número após conjunto de busca): valor')
        self.assertEqual(result,
                         self.manager_pytesseract.run_lucro_liquido_number()[self.filename],
                         'ambas libs trazem o mesmo resultado')

    def test_patrimonio_liquido_monetary(self):
        patrimonio_liquido_monetary = self.manager_pypdf2.run_patrimonio_liquido_monetary()
        result = patrimonio_liquido_monetary[self.filename]

        self.assertEqual(len(result), 0, 'patrimônio líquido (R$): tamanho resultado')
        self.assertEqual(result,
                         self.manager_pytesseract.run_patrimonio_liquido_monetary()[self.filename],
                         'ambas libs trazem o mesmo resultado')

    # @unittest.skip('verificar comentário na planilha de searcher notes')
    def test_patrimonio_liquido_number(self):
        patrimonio_liquido_number = self.manager_pypdf2.run_patrimonio_liquido_number()
        result = patrimonio_liquido_number[self.filename]

        self.assertEqual(len(result), 0, 'patrimônio líquido (número após conjunto de busca): tamanho resultado')
        self.assertEqual(result,
                         self.manager_pytesseract.run_patrimonio_liquido_number()[self.filename],
                         'ambas libs trazem o mesmo resultado')

    def test_roe_monetary(self):
        roe_monetary = self.manager_pypdf2.run_roe_monetary()
        result = roe_monetary[self.filename]

        self.assertEqual(len(result), 0, 'ROE (R$): tamanho resultado')
        self.assertEqual(result,
                         self.manager_pytesseract.run_roe_monetary()[self.filename],
                         'ambas libs trazem o mesmo resultado')

    def test_roe_number(self):
        roe_number = self.manager_pypdf2.run_roe_number()
        result = roe_number[self.filename]

        self.assertEqual(len(result), 0, 'ROE (número após conjunto de busca): tamanho resultado')
        self.assertEqual(result,
                         self.manager_pytesseract.run_roe_number()[self.filename],
                         'ambas libs trazem o mesmo resultado')

    def test_roe_calculate(self):
        roe_calculate = self.manager_pypdf2.run_calculate_roe()
        result = roe_calculate[self.filename]

        # valores do result estao errados por causa dos problemas ao pegar o PL (ver planilha searcher notes)
        self.assertEqual(len(result), 2, 'ROE por cálculo: tamanho resultado')
        self.assertEqual(result,
                         self.manager_pytesseract.run_calculate_roe()[self.filename],
                         'ambas libs trazem o mesmo resultado')


if __name__ == '__main__':
    unittest.main()
