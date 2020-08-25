import PyPDF2
import nltk

from src.plataform import data_dir_scan as dds
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

pdf_reader = PyPDF2.PdfFileReader(dds.data_dir_scan.get_data_directory() + 'ambev_2019_1T.pdf')
# pdf_reader = PyPDF2.PdfFileReader(dds.data_dir_scan.get_data_directory() + 'bancointer_2018_1T.pdf')
# pdf_reader = PyPDF2.PdfFileReader(dds.data_dir_scan.get_data_directory() + 'gerdau_2019_2T.pdf')
# pdf_reader = PyPDF2.PdfFileReader(dds.data_dir_scan.get_data_directory() + 'itau_2019_2T.pdf')
# pdf_reader = PyPDF2.PdfFileReader(dds.data_dir_scan.get_data_directory() + 'weg_2019_2T.pdf')

pdf_text = ''
for i in range(pdf_reader.numPages):
    pdf_page = pdf_reader.getPage(i)
    pdf_text += pdf_page.extractText()

text_tokens = word_tokenize(pdf_text)
tokens_without_stopwords = [token for token in text_tokens if not token in stopwords.words('portuguese')]

# print(tokens_without_stopwords)
print(len(tokens_without_stopwords))
print(len(text_tokens))
