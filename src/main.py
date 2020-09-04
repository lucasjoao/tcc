import PyPDF2
import nltk
import math

from src.plataform import data_dir_scan as dds
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

pt_br = 'portuguese'


def extract_text(pdf_reader):
    pdf_text = ''
    for i in range(pdf_reader.numPages):
        pdf_page = pdf_reader.getPage(i)
        pdf_text += pdf_page.extractText()

    return pdf_text


def preprocess(pdf_text):
    text_sentences = sent_tokenize(pdf_text, pt_br)
    text_sentences_in_tokens = [word_tokenize(sentence) for sentence in text_sentences]

    preprocess_result = []
    for sentence in text_sentences_in_tokens:
        sentence_result = []
        for token in sentence:
            if token not in stopwords.words(pt_br):
                sentence_result.append(token)

        preprocess_result.append(sentence_result)

    return preprocess_result


def stemming(sentences_tokens):
    stemmer = RSLPStemmer()

    stemming_result = []
    for sentence in sentences_tokens:
        sentence_result = []
        for token in sentence:
            sentence_result.append(stemmer.stem(token))

        stemming_result.append(sentence_result)

    return stemming_result


def lucro_liquido_stemming():
    stemmer = RSLPStemmer()
    return frozenset([stemmer.stem('lucro'), stemmer.stem('líquido')])


def patrimonio_liquido_stemming():
    stemmer = RSLPStemmer()
    return frozenset([stemmer.stem('patrimônio'), stemmer.stem('líquido')])


def candidate_sentences(text, searcher_set):
    candidates = []
    for sentence in text:
        if searcher_set < frozenset(sentence):
            candidates.append(sentence)
    return candidates


def is_number(string):
    try:
        number = float(string.replace(',', '.'))
        return (True, number)
    except ValueError:
        return (False, math.nan)


def number_value_searcher(candidate_sentences):
    invalid_positions = frozenset([0, 1])
    results = []
    for sentence in candidate_sentences:
        position = 0
        for token in sentence:
            was_casted, number = is_number(token)
            if was_casted and position not in invalid_positions:
                if sentence[position - 2] == 'r' and sentence[position - 1] == '$':
                    # FIXME: isso pode quebrar se for o último
                    results.append({'number': number, 'possibleSize': sentence[position + 1]})

            position += 1
    return results


def ner(tokens):
    # for token in tokens_without_stopwords:
    #     tagged = nltk.pos_tag(token)
    #     named_ent = nltk.ne_chunk(tagged, binary=False)
    #     print(named_ent)
    pass


pdf_reader = PyPDF2.PdfFileReader(dds.data_dir_scan.get_data_directory() + 'weg_2019_2T.pdf')
pdf_text = extract_text(pdf_reader)
preprocessed_text = preprocess(pdf_text)
stemming_text = stemming(preprocessed_text)
ll_stemming_set = lucro_liquido_stemming()
pl_stemming_set = patrimonio_liquido_stemming()

ll_candidate_sentences = candidate_sentences(stemming_text, ll_stemming_set)
pl_candidate_sentences = candidate_sentences(stemming_text, pl_stemming_set)

print(number_value_searcher(ll_candidate_sentences))
print(number_value_searcher(pl_candidate_sentences))
