class list_helper:

    @staticmethod
    def remove_duplicates(list_of_lists):
        return list(set(map(tuple, list_of_lists)))
