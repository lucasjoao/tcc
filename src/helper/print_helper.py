class print_helper:

    @staticmethod
    def sentence_viewer(sentences):
        """
        Args:
            sentences é uma matriz de sentenças por tokens
        """
        for sentence in sentences:
            print(" ".join(sentence))
            print("\n")

    @staticmethod
    def print_line():
        print(80 * '-')
