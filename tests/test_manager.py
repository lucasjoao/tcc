import unittest
from src import manager as m
from data import data as data


class TestsManager(unittest.TestCase):

    def test_weg_2010_2T(self):
        filename = 'weg_2010_2T.pdf'
        manager = m.manager([filename])

        lucro_liquido_monetary = manager.run_lucro_liquido_monetary()
        result = lucro_liquido_monetary[filename]

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['number'], data.LUCRO_LIQUIDO[filename])

if __name__ == '__main__':
    unittest.main()
