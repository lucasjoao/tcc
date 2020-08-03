# -*- coding: utf-8 -*-
from src.plataform import searcher as searcher


class RoeCalculator:

    def __init__(self, pdf_text):
        self.pdf_text = pdf_text
        self.searcherRoe = searcher.Searcher('ROE', 'retorno on equity')
        self.searcherPatrimonioLiquido = searcher.Searcher('patrimônio líquido')
        self.searcherLucroLiquido = searcher.Searcher('lucro líquido')

    def get_patrimonio_liquido(self):
        return self.searcherPatrimonioLiquido.run(self.pdf_text)

    def get_lucro_liquido(self):
        return self.searcherLucroLiquido.run(self.pdf_text)

    def execute(self):
        roe_value = self.searcherRoe(self.pdf_text)
        if roe_value is None:
            lucro_liquido = self.get_lucro_liquido()
            patrimonio_liquido = self.get_patrimonio_liquido()
            if lucro_liquido is not None and patrimonio_liquido is not None:
                roe_value = (lucro_liquido / patrimonio_liquido) * 100

        return roe_value
