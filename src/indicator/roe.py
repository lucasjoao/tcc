from nltk.stem import RSLPStemmer


class roe:

    def get_target_sets(self):
        # FIXME: chamar stemming global
        stemmer = RSLPStemmer()
        return [frozenset(['roe']),
                frozenset([stemmer.stem('retorno'), stemmer.stem('sobre'),
                           stemmer.stem('patrimônio'), stemmer.stem('líquido')])]

    def calculate(self, lucro_liquido, patrimonio_liquido):
        return (lucro_liquido / patrimonio_liquido) * 100
