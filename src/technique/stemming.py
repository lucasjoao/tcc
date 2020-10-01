import nltk
from nltk.stem import RSLPStemmer


class stemming:

    def __init__(self):
        nltk.download('rslp')
        self.stemmer = RSLPStemmer()

    def stem_word(self, word):
        return self.stemmer.stem(word)
