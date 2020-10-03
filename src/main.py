from src.indicator import roe as roe
from src.indicator import lucro_liquido as ll
from src.indicator import patrimonio_liquido as pl
from src.plataform import pdf_extract as pe
from src.plataform import preprocessor as pp
from src.plataform import filters as f
from src.helper import number_helper as nh
from src.helper import print_helper as ph
from src.helper import result_helper as rh
from src.technique import stemming as s


# TODO SEARCHER
def monetary_value_searcher(candidate_sentences):
    invalid_positions = frozenset([0, 1])
    results = []
    for sentence in candidate_sentences:
        position = 0
        for token in sentence:
            was_casted, number = nh.number_helper.is_number(token)
            if was_casted and position not in invalid_positions:
                if sentence[position - 2] == 'r' and sentence[position - 1] == '$':
                    # FIXME: isso pode quebrar se for o último
                    results.append(rh.result_helper.create_result_item(number, sentence[position + 1]))

            position += 1
    return results


# TODO SEARCHER
def after_target_set_number_value_searcher(candidate_sentences, target_set):
    results = []
    target_set_size = len(target_set)
    for sentence in candidate_sentences:
        curr_position = 0
        for token in sentence:
            possible_result = True
            was_casted, number = nh.number_helper.is_number(token)
            if was_casted:
                for i in range(1, target_set_size + 1):
                    # FIXME: pode quebrar se for o primeiro
                    if sentence[curr_position - i] not in target_set:
                        possible_result = False
                        break

                if possible_result:
                    # FIXME: isso pode quebrar se for o último
                    results.append(rh.result_helper.create_result_item(number, sentence[curr_position + 1]))

            curr_position += 1

    return results


# FIXME: organizer final vai arrumar isso
preprocessor = pp.preprocessor()
lucro_liquido = ll.lucro_liquido()
patrimonio_liquido = pl.patrimonio_liquido()
stemming = s.stemming()
filters = f.filters()


def ll_and_pl_to_file(filename):
    print(filename)
    ph.print_helper.print_line()
    pdf_text = pe.pdf_extract.get_text(filename)
    preprocessed_text = preprocessor.execute(pdf_text)
    stemming_text = stemming.stem_text_matrix(preprocessed_text)
    ll_stemming_set = lucro_liquido.get_target_sets()
    pl_stemming_set = patrimonio_liquido.get_target_sets()

    ll_candidate_sentences = filters.candidate_sentences(stemming_text, ll_stemming_set)
    pl_candidate_sentences = filters.candidate_sentences(stemming_text, pl_stemming_set)

    # filtering
    # FIXME: arrumar ao refatorar
    ll_candidate_sentences = filters.is_searcher_words_in_sequence(ll_candidate_sentences, ll_stemming_set)
    pl_candidate_sentences = filters.is_searcher_words_in_sequence(pl_candidate_sentences, pl_stemming_set)

    ll_false_candidate_sentences = filters.candidate_sentences(ll_candidate_sentences, lucro_liquido.get_filter_sets())
    ll_candidate_sentences = [sentence for sentence in ll_candidate_sentences if sentence not in ll_false_candidate_sentences]

    ll_monetary_dirty_result = monetary_value_searcher(ll_candidate_sentences)
    pl_monetary_dirty_result = monetary_value_searcher(pl_candidate_sentences)

    print('Candidatos (R$) para lucro líquido antes da limpeza:')
    print(ll_monetary_dirty_result)
    print('Candidatos (R$) finais para lucro líquido:')
    print(rh.result_helper.clean_search_result(ll_monetary_dirty_result))
    ph.print_helper.print_line()
    print('Candidatos (R$) para patrimônio líquido antes da limpeza:')
    print(pl_monetary_dirty_result)
    print('Candidatos (R$) finais para patrimônio líquido:')
    print(rh.result_helper.clean_search_result(pl_monetary_dirty_result))
    ph.print_helper.print_line()

    print('Candidatos (numéricos) lucro líquido:')
    # FIXME: arrumar ao refatorar
    ll_number_value_result = after_target_set_number_value_searcher(ll_candidate_sentences, ll_stemming_set[0])
    print(ll_number_value_result)
    print('Candidatos (numéricos) patrimônio líquido:')
    pl_number_value_result = after_target_set_number_value_searcher(pl_candidate_sentences, pl_stemming_set[0])
    print(pl_number_value_result)
    ph.print_helper.print_line()

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
    ph.print_helper.print_line()

    print('Candidato para ROE através de busca')
    # FIXME: fazer busca monetária e de valor ao refatorar
    print(filters.candidate_sentences(stemming_text, roe_indicator.get_target_sets()))
    ph.print_helper.print_line()


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

# TODO: final
# vai ter uma classe Manager que é instanciada no main
# init do manager faz todos os downloads
# add reports no manager
# mando manager executar para o roe
