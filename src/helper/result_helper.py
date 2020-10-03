from src.helper import number_helper as nh


class result_helper:

    @staticmethod
    def create_result_item(number, possible_size):
        normalized_possible_size = possible_size
        was_casted, _ = nh.number_helper.is_number(possible_size)

        if was_casted:
            normalized_possible_size = 'undefined'  # 'undefined' rather than None here solve some problems with types

        return {'number': number, 'possible_size': normalized_possible_size}

    @staticmethod
    def clean_search_result(dirty_result):
        clean_result = []
        for dict_result in dirty_result:
            if dict_result['possible_size'] != 'undefined':
                clean_result.append(dict_result)
        return clean_result
