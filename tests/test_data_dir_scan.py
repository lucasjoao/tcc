
import unittest
from unittest import mock
from src.plataform import data_dir_scan as dds


class TestsDataDirScan(unittest.TestCase):

    @mock.patch('os.getcwd')
    def test_get_data_directory_from_root(self, mock_getcwd):
        mock_getcwd.return_value = '/home/tcc'
        self.assertEqual(dds.data_dir_scan.get_data_directory(), 'data/')
        mock_getcwd.assert_called_once()

    @mock.patch('os.getcwd')
    def test_get_data_directory_from_src(self, mock_getcwd):
        mock_getcwd.return_value = '/home/tcc/src'
        self.assertEqual(dds.data_dir_scan.get_data_directory(), '../data/')
        mock_getcwd.assert_called_once()

    @mock.patch('os.getcwd')
    def test_get_files_name_size(self, mock_getcwd):
        mock_getcwd.return_value = '/home/tcc'
        files_name = dds.data_dir_scan.get_files_name()
        self.assertEqual(len(files_name), 24)
        mock_getcwd.assert_called_once()


if __name__ == '__main__':
    unittest.main()
