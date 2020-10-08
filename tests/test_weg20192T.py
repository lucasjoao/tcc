import unittest
from src import manager as m
from data import data as data


class TestsWeg20192T(unittest.TestCase):

    filename = None
    manager = None

    @classmethod
    def setUpClass(cls):
        cls.filename = 'weg_2019_2T.pdf'
        cls.manager = m.manager([cls.filename])

    @classmethod
    def tearDownClass(cls):
        cls.filename = None
        cls.manager = None

    def test_lucro_liquido_monetary(self):
        lucro_liquido_monetary = self.manager.run_lucro_liquido_monetary()
        result = lucro_liquido_monetary[self.filename]

        self.assertEqual(len(result), 1, 'lucro líquido (R$): tamanho resultado')
        self.assertEqual(result[0]['number'], data.LUCRO_LIQUIDO[self.filename], 'lucro líquido (R$): valor')

    @unittest.skip('verificar comentário na planilha de searcher notes')
    def test_lucro_liquido_number(self):
        lucro_liquido_number = self.manager.run_lucro_liquido_number()
        result = lucro_liquido_number[self.filename]

        self.assertEqual(len(result), 0, 'lucro líquido (número após conjunto de busca): tamanho resultado')

    def test_patrimonio_liquido_monetary(self):
        patrimonio_liquido_monetary = self.manager.run_patrimonio_liquido_monetary()
        result = patrimonio_liquido_monetary[self.filename]

        self.assertEqual(len(result), 0, 'patrimônio líquido (R$): tamanho resultado')

    def test_patrimonio_liquido_number(self):
        patrimonio_liquido_number = self.manager.run_patrimonio_liquido_number()
        result = patrimonio_liquido_number[self.filename]

        self.assertEqual(len(result), 0, 'patrimônio líquido (número após conjunto de busca): tamanho resultado')

    def test_roe_monetary(self):
        roe_monetary = self.manager.run_roe_monetary()
        result = roe_monetary[self.filename]

        self.assertEqual(len(result), 0, 'ROE (R$): tamanho resultado')

    def test_roe_number(self):
        roe_number = self.manager.run_roe_number()
        result = roe_number[self.filename]

        self.assertEqual(len(result), 0, 'ROE (número após conjunto de busca): tamanho resultado')

    def test_roe_calculate(self):
        roe_calculate = self.manager.run_calculate_roe()
        result = roe_calculate[self.filename]

        self.assertEqual(len(result), 0, 'ROE por cálculo: tamanho resultado')


if __name__ == '__main__':
    unittest.main()
