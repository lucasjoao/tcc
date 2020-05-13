# -*- coding: utf-8 -*-
# from src.plataform import searcher as searcher


class RoeCalculator:

    def __init__(self, pdf_text):
        self.pdf_text = pdf_text

    def get_patrimonio_liquido(self):
        return None

    def get_lucro_liquido(self):
        return None

    def execute(self):
        # tentar buscar por roe com searcher (criar um searcher global)
        # se não der, então buscar por patrimonio liquido e lucro liquido
        # cada um com seu searcher
        # se tiver ambos, entao calcular
        # tenho que colocar o cleanup da string em algum lugar
        # ler sobre empty constructor python, aqui deve vir o pdf_text
        # gets nao possuem visibilidade publica, como?
        pass
