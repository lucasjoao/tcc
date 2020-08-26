import PyPDF2
import nltk

from src.plataform import data_dir_scan as dds
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

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

stemmer = RSLPStemmer()
text_tokens_stemming = ''
for token in tokens_without_stopwords:
    text_tokens_stemming += stemmer.stem(token) + ' '

for token in tokens_without_stopwords:
    tagged = nltk.pos_tag(token)
    named_ent = nltk.ne_chunk(tagged, binary=False)
    print(named_ent)

# print(tokens_without_stopwords)
# print(len(tokens_without_stopwords))
# print(len(text_tokens))
# print(text_tokens_stemming)
