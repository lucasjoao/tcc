# -*- coding: utf-8 -*-
"""Funcoes auxiliares para interagir com o diretorio 'data' do repositorio que possui os
relatorios utilizados nos experimentos"""

import os


class data_dir_scan:
    """Classe que possui as funcoes auxiliares"""

    @staticmethod
    def get_data_directory():
        """Retorna uma string que contem o diretorio 'data' que possui os relatorios
        com base na localizacao em que o metodo foi chamado

        Returns:
            String com o diretorio data
        """
        data_directory = 'data/'
        current_directory = os.getcwd()
        if 'src' in current_directory or 'tests' in current_directory:
            data_directory = '../data/'
        return data_directory

    @staticmethod
    def get_files_name():
        """Retorna os arquivos .PDFs presente no diretorio 'data'

        Returns:
            Lista de string com o nome dos arquivos .PDFs
        """
        data_directory = data_dir_scan.get_data_directory()
        return [item for item in os.listdir(data_directory) if '.pdf' in item]
