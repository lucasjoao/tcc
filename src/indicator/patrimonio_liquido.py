from src.technique import stemming as s


class patrimonio_liquido:

    def __init__(self):
        self.stemmer = s.stemming()

    def get_target_sets(self):
        return [frozenset([self.stemmer.stem_word('patrimônio'), self.stemmer.stem_word('líquido')])]

    def get_filter_sets(self):
        return [frozenset([])]
