# -*- coding: utf-8 -*-
from src.plataform import searcher as searcher


class RoeCalculator:

    def __init__(self, pdf_text):
        self.pdf_text = pdf_text
        self.searcherRoe = searcher.Searcher(['ROE', 'retorno on equity'])
        self.searcherPatrimonioLiquido = searcher.Searcher(['patrimônio líquido'])
        self.searcherLucroLiquido = searcher.Searcher(['lucro líquido'])

    def get_patrimonio_liquido(self):
        patrimonio_liquido = self.searcherPatrimonioLiquido.run(self.pdf_text)
        if patrimonio_liquido is not None:
            patrimonio_liquido = float(patrimonio_liquido)
        return patrimonio_liquido

    # TODO: testar isso e get_patrimonio_liquido?
    def get_lucro_liquido(self):
        lucro_liquido = self.searcherLucroLiquido.run(self.pdf_text)
        if lucro_liquido is not None:
            lucro_liquido = float(lucro_liquido)
        return lucro_liquido

    def execute(self):
        roe_value = self.searcherRoe.run(self.pdf_text)
        if roe_value is None:
            lucro_liquido = self.get_lucro_liquido()
            patrimonio_liquido = self.get_patrimonio_liquido()
            if lucro_liquido is not None and patrimonio_liquido is not None:
                roe_value = (lucro_liquido / patrimonio_liquido) * 100
                roe_value = round(roe_value, 2)

        return roe_value
