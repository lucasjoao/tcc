import nltk
import math
import re

from src.indicator import roe as roe
from src.plataform import pdf_extract as pe
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


def dividendos_stemming():
    stemmer = RSLPStemmer()
    return frozenset([stemmer.stem('dividendos')])


def divida_stemming():
    stemmer = RSLPStemmer()
    return frozenset([stemmer.stem('dívida')])


def imposto_stemming():
    stemmer = RSLPStemmer()
    return frozenset([stemmer.stem('imposto')])


def ebitda_stemming():
    stemmer = RSLPStemmer()
    return frozenset([stemmer.stem('ebitda')])


def recuperacao_stemming():
    stemmer = RSLPStemmer()
    return frozenset([stemmer.stem('recuperação')])


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
    if string.count('.') <= 1:
        try:
            # works fine with '1234', '1234.12' and '1234.0'
            number = float(string.replace(',', '.'))
            return (True, number)
        except ValueError:
            return (False, math.nan)
    else:
        return is_number_with_more_dots(string)


def is_number_with_more_dots(string):
    try:
        # works fine with '1.234.567'
        number = float(string.replace('.', ''))
        return (True, number)
    except ValueError:
        return is_number_with_more_dots_and_decimal(string)


# FIXME: se isso daqui jogar exception no float, entao pode dar ruim
def is_number_with_more_dots_and_decimal(string):
    # works fine with '1.234.567.89'
    if re.fullmatch(r'.*\.\d{2}', string) is not None:
        dots_number = string.count('.')
        number = float(string.replace('.', '', dots_number - 1))
        return (True, number)
    else:
        return (False, math.nan)


def create_result_item(number, possible_size):
    normalized_possible_size = possible_size
    was_casted, _ = is_number(possible_size)

    if was_casted:
        # FIXME: undefined aqui ao inves de None resolve erros por causa da tipagem
        normalized_possible_size = 'undefined'

    return {'number': number, 'possible_size': normalized_possible_size}


def monetary_value_searcher(candidate_sentences):
    invalid_positions = frozenset([0, 1])
    results = []
    for sentence in candidate_sentences:
        position = 0
        for token in sentence:
            was_casted, number = is_number(token)
            if was_casted and position not in invalid_positions:
                if sentence[position - 2] == 'r' and sentence[position - 1] == '$':
                    # FIXME: isso pode quebrar se for o último
                    results.append(create_result_item(number, sentence[position + 1]))

            position += 1
    return results


def after_target_set_number_value_searcher(candidate_sentences, target_set):
    results = []
    target_set_size = len(target_set)
    for sentence in candidate_sentences:
        curr_position = 0
        for token in sentence:
            possible_result = True
            was_casted, number = is_number(token)
            if was_casted:
                for i in range(1, target_set_size + 1):
                    # FIXME: pode quebrar se for o primeiro
                    if sentence[curr_position - i] not in target_set:
                        possible_result = False
                        break

                if possible_result:
                    # FIXME: isso pode quebrar se for o último
                    results.append(create_result_item(number, sentence[curr_position + 1]))

            curr_position += 1

    return results


def clean_search_result(dirty_result):
    clean_result = []
    for dict_result in dirty_result:
        if not is_number(dict_result['possible_size'])[0]:
            clean_result.append(dict_result)
    return clean_result


def sentence_viewer(sentences):
    for sentence in sentences:
        print(" ".join(sentence))
        print("\n")


def ll_and_pl_to_file(filename):
    print(filename)
    print(80 * '-')
    pdf_text = pe.pdf_extract.get_text(filename)
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

    ll_false_candidate_sentences = candidate_sentences(ll_candidate_sentences, dividendos_stemming())
    ll_candidate_sentences = [sentence for sentence in ll_candidate_sentences if sentence not in ll_false_candidate_sentences]

    ll_false_candidate_sentences = candidate_sentences(ll_candidate_sentences, divida_stemming())
    ll_candidate_sentences = [sentence for sentence in ll_candidate_sentences if sentence not in ll_false_candidate_sentences]

    ll_false_candidate_sentences = candidate_sentences(ll_candidate_sentences, imposto_stemming())
    ll_candidate_sentences = [sentence for sentence in ll_candidate_sentences if sentence not in ll_false_candidate_sentences]

    ll_false_candidate_sentences = candidate_sentences(ll_candidate_sentences, ebitda_stemming())
    ll_candidate_sentences = [sentence for sentence in ll_candidate_sentences if sentence not in ll_false_candidate_sentences]

    ll_false_candidate_sentences = candidate_sentences(ll_candidate_sentences, recuperacao_stemming())
    ll_candidate_sentences = [sentence for sentence in ll_candidate_sentences if sentence not in ll_false_candidate_sentences]

    ll_monetary_dirty_result = monetary_value_searcher(ll_candidate_sentences)
    pl_monetary_dirty_result = monetary_value_searcher(pl_candidate_sentences)

    print('Candidatos (R$) para lucro líquido antes da limpeza:')
    print(ll_monetary_dirty_result)
    print('Candidatos (R$) finais para lucro líquido:')
    print(clean_search_result(ll_monetary_dirty_result))
    print(80 * '-')
    print('Candidatos (R$) para patrimônio líquido antes da limpeza:')
    print(pl_monetary_dirty_result)
    print('Candidatos (R$) finais para patrimônio líquido:')
    print(clean_search_result(pl_monetary_dirty_result))
    print(80 * '-')

    print('Candidatos (numéricos) lucro líquido:')
    ll_number_value_result = after_target_set_number_value_searcher(ll_candidate_sentences, ll_stemming_set)
    print(ll_number_value_result)
    print('Candidatos (numéricos) patrimônio líquido:')
    pl_number_value_result = after_target_set_number_value_searcher(pl_candidate_sentences, pl_stemming_set)
    print(pl_number_value_result)
    print(80 * '-')

    roe_indicator = roe.roe()

    # FIXME: não ser repetitivo
    # FIXME: considerar escala
    # FIXME: deveria entrar no pós?
    print('Possível valor de ROE')
    if len(ll_monetary_dirty_result):
        if len(pl_monetary_dirty_result):
            for ll_dict in ll_monetary_dirty_result:
                for pl_dict in pl_monetary_dirty_result:
                    print(roe_indicator.calculate(ll_dict['number'], pl_dict['number']))

        if len(pl_number_value_result):
            for ll_dict in ll_monetary_dirty_result:
                for pl_dict in pl_number_value_result:
                    print(roe_indicator.calculate(ll_dict['number'], pl_dict['number']))

    if len(ll_number_value_result):
        if len(pl_monetary_dirty_result):
            for ll_dict in ll_number_value_result:
                for pl_dict in pl_monetary_dirty_result:
                    print(roe_indicator.calculate(ll_dict['number'], pl_dict['number']))

        if len(pl_number_value_result):
            for ll_dict in ll_number_value_result:
                for pl_dict in pl_number_value_result:
                    print(roe_indicator.calculate(ll_dict['number'], pl_dict['number']))
    print(80 * '-')

ll_and_pl_to_file('weg_2010_2T.pdf')
ll_and_pl_to_file('weg_2015_1T.pdf')
ll_and_pl_to_file('weg_2017_2T.pdf')
ll_and_pl_to_file('weg_2019_2T.pdf')
ll_and_pl_to_file('gerdau_2017_1T.pdf')
ll_and_pl_to_file('gerdau_2015_3T.pdf')
ll_and_pl_to_file('engie_2019_2T.pdf')
ll_and_pl_to_file('engie_2020_2T.pdf')
ll_and_pl_to_file('fleury_2019_3T.pdf')
ll_and_pl_to_file('fleury_2020_2T.pdf')
