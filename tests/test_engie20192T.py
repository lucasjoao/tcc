import unittest
from src import manager as m
from src.helper import result_helper as rh
from data import data as data


class TestsEngie20192T(unittest.TestCase):

    filename = None
    manager = None

    @classmethod
    def setUpClass(cls):
        cls.filename = 'engie_2019_2T.pdf'
        cls.manager = m.manager([cls.filename])

    @classmethod
    def tearDownClass(cls):
        cls.filename = None
        cls.manager = None

    def test_lucro_liquido_monetary(self):
        lucro_liquido_monetary = self.manager.run_lucro_liquido_monetary()
        result = lucro_liquido_monetary[self.filename]
        numbers_from_result = rh.result_helper.get_numbers_as_list(result)

        self.assertEqual(len(result), 3, 'lucro líquido (R$): tamanho resultado')
        self.assertIn(data.LUCRO_LIQUIDO[self.filename], numbers_from_result, 'lucro líquido (R$): valor')

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
