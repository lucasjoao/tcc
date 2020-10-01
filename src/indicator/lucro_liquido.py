from src.technique import stemming as s


class lucro_liquido:

    def __init__(self):
        self.stemmer = s.stemming()

    def get_target_sets(self):
        return [frozenset([self.stemmer.stem_word('lucro'), self.stemmer.stem_word('líquido')])]
