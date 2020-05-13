# -*- coding: utf-8 -*-


class Searcher:

    def __init__(self, words):
        self.words = words

    def run(self, input_text):
        for word in self.words:
            word_index = input_text.find(word)
            if word_index != -1:
                print(word + ' encontrado no texto na posição ' + str(word_index))
                fix_word_index = word_index + len(word) - 1  # because of compound words
                text_after_found = input_text[fix_word_index:]
                return text_after_found.split()[1]
        # questão lowercase e tal
        return 'Nada encontrado!'
