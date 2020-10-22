from src.helper import number_helper as nh


class result_helper:

    __undefined = 'undefined'

    @staticmethod
    def create_result_item(number, possible_size):
        normalized_possible_size = possible_size
        was_casted, _ = nh.number_helper.is_number(possible_size)

        if was_casted:
            normalized_possible_size = result_helper.__undefined  # not None here solve some problems with types

        return {'number': number, 'possible_size': normalized_possible_size}

    @staticmethod
    def clean_search_result(dirty_result):
        clean_result = []
        for dict_result in dirty_result:
            if dict_result['possible_size'] != result_helper.__undefined:
                clean_result.append(dict_result)
        return clean_result

    @staticmethod
    def get_numbers_as_list(result_item_list):
        numbers_result = []
        for result_item in result_item_list:
            for key, number in result_item.items():
                if key == 'number':
                    numbers_result.append(number)
        return numbers_result
