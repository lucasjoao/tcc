import os


class data_dir_scan:

    __src = 'src'
    __tests = 'tests'

    @staticmethod
    def get_data_directory():
        current_directory = os.getcwd()
        directory_splitted = current_directory.split('/')

        if 'data' == directory_splitted[-1]:  # last element from list
            return './'

        directory_founded = None
        if data_dir_scan.__src in directory_splitted:
            directory_founded = data_dir_scan.__src
        elif data_dir_scan.__tests in current_directory:
            directory_founded = data_dir_scan.__tests

        if directory_founded is None:
            raise Exception('Diretório inválido!')

        position = directory_splitted.index(directory_founded)
        levels_below = len(directory_splitted) - position
        return ('../' * levels_below) + 'data/'
