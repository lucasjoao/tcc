import unittest
from src import manager as m
from src.helper import result_helper as rh
from data import data as data


class TestsWeg20192T(unittest.TestCase):

    filename = None
    manager_pypdf2 = None

    @classmethod
    def setUpClass(cls):
        cls.filename = 'weg_2019_2T.pdf'
        cls.manager_pypdf2 = m.manager([cls.filename], 'pypdf2')

    @classmethod
    def tearDownClass(cls):
        cls.filename = None
        cls.manager_pypdf2 = None

    def test_lucro_liquido_monetary(self):
        lucro_liquido_monetary_pypdf2 = self.manager_pypdf2.run_lucro_liquido_monetary()
        result_pypdf2 = lucro_liquido_monetary_pypdf2[self.filename]
        numbers_from_result_pypdf2 = rh.result_helper.get_numbers_as_list(result_pypdf2)

        self.assertEqual(len(result_pypdf2), 1, 'lucro líquido (R$): tamanho resultado (pypdf2)')
        self.assertIn(data.LUCRO_LIQUIDO[self.filename], numbers_from_result_pypdf2,
                      'lucro líquido (R$): valor (pypdf2)')

    def test_lucro_liquido_number(self):
        lucro_liquido_number_pypdf2 = self.manager_pypdf2.run_lucro_liquido_number()
        result_pypdf2 = lucro_liquido_number_pypdf2[self.filename]
        numbers_from_result_pypdf2 = rh.result_helper.get_numbers_as_list(result_pypdf2)

        self.assertEqual(len(result_pypdf2), 1,
                         'lucro líquido (número após conjunto de busca): tamanho resultado (pypdf2)')
        self.assertNotIn(data.LUCRO_LIQUIDO[self.filename], numbers_from_result_pypdf2,
                         'lucro líquido (número após conjunto de busca): valor (pypdf2)')

    def test_patrimonio_liquido_monetary(self):
        patrimonio_liquido_monetary = self.manager_pypdf2.run_patrimonio_liquido_monetary()
        result = patrimonio_liquido_monetary[self.filename]

        self.assertEqual(len(result), 0, 'patrimônio líquido (R$): tamanho resultado')

    def test_patrimonio_liquido_number(self):
        patrimonio_liquido_number_pypdf2 = self.manager_pypdf2.run_patrimonio_liquido_number()
        result_pypdf2 = patrimonio_liquido_number_pypdf2[self.filename]

        self.assertEqual(len(result_pypdf2), 0,
                         'patrimônio líquido (número após conjunto de busca): tamanho resultado (pypdf2)')

    def test_roe_monetary(self):
        roe_monetary = self.manager_pypdf2.run_roe_monetary()
        result = roe_monetary[self.filename]

        self.assertEqual(len(result), 0, 'ROE (R$): tamanho resultado')

    def test_roe_number(self):
        roe_number = self.manager_pypdf2.run_roe_number()
        result = roe_number[self.filename]

        self.assertEqual(len(result), 0, 'ROE (número após conjunto de busca): tamanho resultado')

    def test_roe_calculate(self):
        roe_calculate_pypdf2 = self.manager_pypdf2.run_calculate_roe()
        result_pypdf2 = roe_calculate_pypdf2[self.filename]

        self.assertEqual(len(result_pypdf2), 0, 'ROE por cálculo: tamanho resultado (pypdf2)')


if __name__ == '__main__':
    unittest.main()
