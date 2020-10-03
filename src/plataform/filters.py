class filters:

    def candidate_sentences(self, text, target_sets):
        candidates = []
        for sentence in text:
            for target_set in target_sets:
                if target_set < frozenset(sentence):
                    candidates.append(sentence)
        return candidates

    def is_searcher_words_in_sequence(self, candidates, target_sets):
        candidates_filtered = []
        for sentence in candidates:
            for target_set in target_sets:
                first_searcher_element, *_ = target_set
                target_set_size = len(target_set)
                position = sentence.index(first_searcher_element)

                hits = 1
                for i in range(1, target_set_size):
                    if sentence[position + i] in target_set or sentence[position - i] in target_set:
                        hits += 1

                if target_set_size == hits:
                    candidates_filtered.append(sentence)
        return candidates_filtered
