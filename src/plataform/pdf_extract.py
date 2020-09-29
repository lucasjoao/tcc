import PyPDF2

from src.plataform import data_dir_scan as dds


class pdf_extract:

    @staticmethod
    def get_text(filename):
        pdf_reader = PyPDF2.PdfFileReader(dds.data_dir_scan.get_data_directory() + filename)

        pdf_text = ''
        for i in range(pdf_reader.numPages):
            pdf_page = pdf_reader.getPage(i)
            pdf_text += pdf_page.extractText()

        return pdf_text
