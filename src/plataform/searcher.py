# -*- coding: utf-8 -*-


# TODO talvez alterar para receber texto no construtor e aí o run receber o que se quer buscar
class Searcher:

    def __init__(self, words):
        self.words = [word.lower() for word in words]

    def run(self, input_text):
        input_text_lower = input_text.lower()
        for word in self.words:
            word_index = input_text_lower.find(word)
            if word_index != -1:
                print(word + ' encontrado no texto na posição ' + str(word_index))
                fix_word_index = word_index + len(word) - 1  # because of compound words
                text_after_found = input_text[fix_word_index:]
                return text_after_found.split()[1]
        return None
