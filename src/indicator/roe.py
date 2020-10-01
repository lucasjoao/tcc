from src.technique import stemming as s


class roe:

    def __init__(self):
        self.stemmer = s.stemming()

    def get_target_sets(self):
        return [frozenset(['roe']),
                frozenset([self.stemmer.stem_word('retorno'), self.stemmer.stem_word('sobre'),
                           self.stemmer.stem_word('patrimônio'), self.stemmer.stem_word('líquido')])]

    def calculate(self, lucro_liquido, patrimonio_liquido):
        return (lucro_liquido / patrimonio_liquido) * 100
