from src.helper import list_helper as lh


class filters:

    def candidate_sentences(self, text, target_sets):
        candidates = []
        for sentence in text:
            for target_set in target_sets:
                empty_target_set = len(target_set) == 0
                if not empty_target_set and target_set.issubset(frozenset(sentence)):
                    candidates.append(sentence)
        return candidates

    def is_searcher_words_in_sequence(self, candidates, target_sets):
        candidates_filtered = []
        for sentence in candidates:
            for target_set in target_sets:
                first_searcher_element, *_ = target_set
                target_set_size = len(target_set)
                positions = [i for i, token in enumerate(sentence) if token == first_searcher_element]

                for position in positions:
                    hits = 1
                    for i in range(1, target_set_size):
                        try:
                            is_hit = sentence[position + i] in target_set or sentence[position - i] in target_set
                        except IndexError:
                            is_hit = False
                        if is_hit:
                            hits += 1

                    if target_set_size == hits:
                        candidates_filtered.append(sentence)
        return lh.list_helper.remove_duplicates_list_of_lists(candidates_filtered)
