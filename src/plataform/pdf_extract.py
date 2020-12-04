import PyPDF2
import pytesseract

from pdf2image import convert_from_path
from src.plataform import data_dir_scan as dds


class pdf_extract:

    @staticmethod
    def get_text_pypdf2(filename):
        pdf_reader = PyPDF2.PdfFileReader(pdf_extract.__path_from_filename(filename))

        pdf_text = ''
        for i in range(pdf_reader.numPages):
            pdf_page = pdf_reader.getPage(i)
            pdf_text += pdf_page.extractText()

        return pdf_text

    @staticmethod
    def __path_from_filename(filename):
        return dds.data_dir_scan.get_data_directory() + filename

    @staticmethod
    def get_text_pytesseract(filename):
        pages = convert_from_path(pdf_extract.__path_from_filename(filename), 500)

        config_to_speed_up = '-c tessedit_do_invert=0'

        pdf_text = ''
        for page in pages:
            pdf_text = pdf_text + ' ' + pytesseract.image_to_string(page, lang='por', config=config_to_speed_up)

        return pdf_text
