import os


class data_dir_scan:

    @staticmethod
    def get_data_directory():
        data_directory = 'data/'
        if 'src' in os.getcwd():
            data_directory = '../data/'
        return data_directory

    @staticmethod
    def get_files_name():
        data_directory = data_dir_scan.get_data_directory()
        return [item for item in os.listdir(data_directory) if '.pdf' in item]
