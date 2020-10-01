import nltk
from nltk.stem import RSLPStemmer


class stemming:

    def __init__(self):
        nltk.download('rslp')
        self.stemmer = RSLPStemmer()

    def stem_word(self, word):
        return self.stemmer.stem(word)

    def stem_text_matrix(self, text_matrix):
        """
        Args
            text_matrix é o resultado da etapa de pré-processamento
        """
        result = []
        for sentence in text_matrix:
            sentence_result = [self.stem_word(token) for token in sentence]
            result.append(sentence_result)

        return result
