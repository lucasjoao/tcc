class list_helper:

    @staticmethod
    def remove_duplicates_list_of_lists(list_of_lists):
        return list(set(map(tuple, list_of_lists)))

    @staticmethod
    def remove_duplicates_list_of_dicts(list_of_dicts):
        # thanks https://stackoverflow.com/questions/9427163/remove-duplicate-dict-in-list-in-python
        return [dict(t) for t in {tuple(d.items()) for d in list_of_dicts}]
