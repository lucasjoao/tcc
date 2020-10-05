import unittest
from src import manager as m
from data import data as data


class TestsManager(unittest.TestCase):

    def test_weg_2010_2T(self):
        filename = 'weg_2010_2T.pdf'
        manager = m.manager([filename])

        lucro_liquido_monetary = manager.run_lucro_liquido_monetary()
        result = lucro_liquido_monetary[filename]

        self.assertEqual(len(result), 1, 'lucro líquido (R$): tamanho resultado')
        self.assertEqual(result[0]['number'], data.LUCRO_LIQUIDO[filename], 'lucro líquido (R$): valor')

        lucro_liquido_number = manager.run_lucro_liquido_number()
        result = lucro_liquido_number[filename]

        self.assertEqual(len(result), 0, 'lucro líquido (número após conjunto de busca): tamanho resultado')

        patrimonio_liquido_monetary = manager.run_patrimonio_liquido_monetary()
        result = patrimonio_liquido_monetary[filename]

        self.assertEqual(len(result), 0, 'patrimônio líquido (R$): tamanho resultado')

        patrimonio_liquido_number = manager.run_patrimonio_liquido_number()
        result = patrimonio_liquido_number[filename]

        self.assertEqual(len(result), 0, 'patrimônio líquido (número após conjunto de busca): tamanho resultado')

        roe_monetary = manager.run_roe_monetary()
        result = roe_monetary[filename]

        self.assertEqual(len(result), 0, 'ROE (R$): tamanho resultado')

        roe_number = manager.run_roe_number()
        result = roe_number[filename]

        self.assertEqual(len(result), 0, 'ROE (número após conjunto de busca): tamanho resultado')

        roe_calculate = manager.run_calculate_roe()
        result = roe_calculate[filename]

        self.assertEqual(len(result), 0, 'ROE por cálculo: tamanho resultado')

if __name__ == '__main__':
    unittest.main()
