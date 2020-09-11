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


def ir_stemming():
    stemmer = RSLPStemmer()
    return frozenset([stemmer.stem('imposto'), stemmer.stem('renda')])


def receita_operacional_liquida_stemming():
    stemmer = RSLPStemmer()
    return frozenset([stemmer.stem('receita'), stemmer.stem('operacional'), stemmer.stem('líquida')])


def ticket_stemming():
    stemmer = RSLPStemmer()
    return frozenset([stemmer.stem('wege3')])


def ativos_fixos_stemming():
    stemmer = RSLPStemmer()
    return frozenset([stemmer.stem('ativos'), stemmer.stem('fixos')])


def investimentos_stemming():
    stemmer = RSLPStemmer()
    return frozenset([stemmer.stem('investimentos')])


def variacao_stemming():
    stemmer = RSLPStemmer()
    return frozenset([stemmer.stem('variação')])


def candidate_sentences(text, searcher_set):
    candidates = []
    for sentence in text:
        if searcher_set < frozenset(sentence):
            candidates.append(sentence)
    return candidates


def is_searcher_words_in_sequence(candidates, searcher_set):
    candidates_filtered = []
    for sentence in candidates:
        first_searcher_element, *_ = searcher_set
        searcher_set_size = len(searcher_set)
        position = sentence.index(first_searcher_element)

        hits = 0
        for i in range(1, searcher_set_size):
            if sentence[position + i] in searcher_set or sentence[position - i] in searcher_set:
                hits += 1

        if (searcher_set_size - 1) == hits:
            candidates_filtered.append(sentence)

    return candidates_filtered


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


def sentence_viewer(sentences):
    for sentence in sentences:
        print(" ".join(sentence))
        print("\n")


def ll_and_pl_to_file(filename):
    print(filename)
    pdf_reader = PyPDF2.PdfFileReader(dds.data_dir_scan.get_data_directory() + filename)
    pdf_text = extract_text(pdf_reader)
    preprocessed_text = preprocess(pdf_text)
    stemming_text = stemming(preprocessed_text)
    ll_stemming_set = lucro_liquido_stemming()
    pl_stemming_set = patrimonio_liquido_stemming()

    ll_candidate_sentences = candidate_sentences(stemming_text, ll_stemming_set)
    pl_candidate_sentences = candidate_sentences(stemming_text, pl_stemming_set)

    # filtering
    ll_candidate_sentences = is_searcher_words_in_sequence(ll_candidate_sentences, ll_stemming_set)
    pl_candidate_sentences = is_searcher_words_in_sequence(pl_candidate_sentences, pl_stemming_set)

    ll_false_candidate_sentences = candidate_sentences(ll_candidate_sentences, ir_stemming())
    ll_candidate_sentences = [sentence for sentence in ll_candidate_sentences if sentence not in ll_false_candidate_sentences]

    ll_false_candidate_sentences = candidate_sentences(ll_candidate_sentences, receita_operacional_liquida_stemming())
    ll_candidate_sentences = [sentence for sentence in ll_candidate_sentences if sentence not in ll_false_candidate_sentences]

    ll_false_candidate_sentences = candidate_sentences(ll_candidate_sentences, ticket_stemming())
    ll_candidate_sentences = [sentence for sentence in ll_candidate_sentences if sentence not in ll_false_candidate_sentences]

    ll_false_candidate_sentences = candidate_sentences(ll_candidate_sentences, ativos_fixos_stemming())
    ll_candidate_sentences = [sentence for sentence in ll_candidate_sentences if sentence not in ll_false_candidate_sentences]

    ll_false_candidate_sentences = candidate_sentences(ll_candidate_sentences, investimentos_stemming())
    ll_candidate_sentences = [sentence for sentence in ll_candidate_sentences if sentence not in ll_false_candidate_sentences]

    ll_false_candidate_sentences = candidate_sentences(ll_candidate_sentences, variacao_stemming())
    ll_candidate_sentences = [sentence for sentence in ll_candidate_sentences if sentence not in ll_false_candidate_sentences]

    print(number_value_searcher(ll_candidate_sentences))
    print(number_value_searcher(pl_candidate_sentences))


ll_and_pl_to_file('weg_2010_2T.pdf')
ll_and_pl_to_file('weg_2015_1T.pdf')
ll_and_pl_to_file('weg_2017_2T.pdf')
ll_and_pl_to_file('weg_2019_2T.pdf')
ll_and_pl_to_file('gerdau_2017_1T.pdf')
# TODO: preciso de mais 5 relatórios (1 gerdau e 4 de duas empresas)
