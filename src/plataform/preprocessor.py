from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords


class preprocessor:

    __pt_br = 'portuguese'

    def execute(self, text):
        text_sentences = sent_tokenize(text, self.__pt_br)
        text_sentences_in_tokens = [word_tokenize(sentence) for sentence in text_sentences]

        stopwords_pt_br = stopwords.words(self.__pt_br)
        preprocess_result = []

        for sentence in text_sentences_in_tokens:
            sentence_result = [token for token in sentence if token not in stopwords_pt_br]
            preprocess_result.append(sentence_result)

        return preprocess_result
