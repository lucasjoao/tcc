from src.helper import number_helper as nh
from src.helper import result_helper as rh


class searcher:

    def monetary_value(self, candidate_sentences):
        invalid_positions = frozenset([0, 1])

        results = []
        for sentence in candidate_sentences:
            position = 0
            for token in sentence:
                was_casted, number = nh.number_helper.is_number(token)
                if was_casted and position not in invalid_positions:
                    if sentence[position - 2] == 'r' and sentence[position - 1] == '$':
                        results.append(self.__safe_create_result_item(number, sentence, position))

                position += 1

        return results

    def after_target_set_number_value(self, candidate_sentences, target_sets):
        results = []
        for target_set in target_sets:
            target_set_size = len(target_set)
            for sentence in candidate_sentences:
                curr_position = 0
                for token in sentence:
                    possible_result = True

                    was_casted, number = nh.number_helper.is_number(token)
                    if was_casted:

                        for i in range(1, target_set_size + 1):
                            lookup_position = curr_position - i
                            if lookup_position < 0 or sentence[lookup_position] not in target_set:
                                possible_result = False
                                break

                        if possible_result:
                            results.append(self.__safe_create_result_item(number, sentence, curr_position))

                    curr_position += 1

        return results

    def __safe_create_result_item(self, number, sentence, position):
        result_item = {}
        try:
            result_item = rh.result_helper.create_result_item(number, sentence[position + 1])
        except IndexError:
            result_item = rh.result_helper.create_result_item(number, 'undefined')
        return result_item
