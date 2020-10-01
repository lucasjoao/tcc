from src.technique import stemming as s


class lucro_liquido:

    def __init__(self):
        self.stemmer = s.stemming()

    def get_target_sets(self):
        return [frozenset([self.stemmer.stem_word('lucro'), self.stemmer.stem_word('líquido')])]

    def get_filter_sets(self):
        return [frozenset([self.stemmer.stem_word('imposto'), self.stemmer.stem_word('renda')]),
                frozenset([self.stemmer.stem_word('receita'), self.stemmer.stem_word('operacional'),
                           self.stemmer.stem_word('líquida')]),
                frozenset([self.stemmer.stem_word('wege3')]),
                frozenset([self.stemmer.stem_word('ativos'), self.stemmer.stem_word('fixos')]),
                frozenset([self.stemmer.stem_word('investimentos')]),
                frozenset([self.stemmer.stem_word('variação')]),
                frozenset([self.stemmer.stem_word('dividendos')]),
                frozenset([self.stemmer.stem_word('dívida')]),
                frozenset([self.stemmer.stem_word('imposto')]),
                frozenset([self.stemmer.stem_word('ebitda')]),
                frozenset([self.stemmer.stem_word('recuperação')])]
