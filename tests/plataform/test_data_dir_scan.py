
import unittest
from unittest import mock
from src.plataform import data_dir_scan as dds


class TestsDataDirScan(unittest.TestCase):

    @mock.patch('os.getcwd')
    def test_get_data_directory_from_root(self, mock_getcwd):
        mock_getcwd.return_value = '/home/tcc'
        self.assertRaises(Exception, dds.data_dir_scan.get_data_directory)
        mock_getcwd.assert_called_once()

    @mock.patch('os.getcwd')
    def test_get_data_directory_from_tests(self, mock_getcwd):
        mock_getcwd.return_value = '/home/tcc/tests'
        self.assertEqual(dds.data_dir_scan.get_data_directory(), '../data/')
        mock_getcwd.assert_called_once()

    @mock.patch('os.getcwd')
    def test_get_data_directory_from_src_with_levels_belows(self, mock_getcwd):
        mock_getcwd.return_value = '/home/tcc/src/plataform'
        self.assertEqual(dds.data_dir_scan.get_data_directory(), '../../data/')
        mock_getcwd.assert_called_once()

    @mock.patch('os.getcwd')
    def test_get_data_directory_from_data(self, mock_getcwd):
        mock_getcwd.return_value = '/home/tcc/data'
        self.assertEqual(dds.data_dir_scan.get_data_directory(), './')
        mock_getcwd.assert_called_once()


if __name__ == '__main__':
    unittest.main()
