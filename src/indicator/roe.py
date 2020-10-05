from src.technique import stemming as s


class roe:

    def __init__(self):
        self.stemmer = s.stemming()

    def get_target_sets(self):
        return [frozenset(['roe']),
                frozenset([self.stemmer.stem_word('retorno'), self.stemmer.stem_word('sobre'),
                           self.stemmer.stem_word('patrimônio'), self.stemmer.stem_word('líquido')])]

    def get_filter_sets(self):
        pass

    def calculate(self, lucro_liquido, patrimonio_liquido):
        # FIXME: considerar escala na hora de calcular
        return (lucro_liquido / patrimonio_liquido) * 100

    def calculate_iterating(self, lucro_liquido_result_list, patrimonio_liquido_result_list):
        result = []
        for lucro_liquido in lucro_liquido_result_list:
            for patrimonio_liquido in patrimonio_liquido_result_list:
                result.append(self.calculate(lucro_liquido['number'], patrimonio_liquido['number']))
        return result
