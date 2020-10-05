from src import manager as m


# FIXME: organizer final vai arrumar isso

patrimonio_liquido = pl.patrimonio_liquido()



def ll_and_pl_to_file(filename):
    ll_stemming_set = lucro_liquido.get_target_sets()
    pl_stemming_set = patrimonio_liquido.get_target_sets()

    ll_candidate_sentences = filters.candidate_sentences(stemming_text, ll_stemming_set)
    pl_candidate_sentences = filters.candidate_sentences(stemming_text, pl_stemming_set)

    ll_candidate_sentences = filters.is_searcher_words_in_sequence(ll_candidate_sentences, ll_stemming_set)
    pl_candidate_sentences = filters.is_searcher_words_in_sequence(pl_candidate_sentences, pl_stemming_set)

    ll_false_candidate_sentences = filters.candidate_sentences(ll_candidate_sentences, lucro_liquido.get_filter_sets())
    ll_candidate_sentences = [sentence for sentence in ll_candidate_sentences if sentence not in ll_false_candidate_sentences]

    ll_monetary_dirty_result = searcher.monetary_value(ll_candidate_sentences)
    pl_monetary_dirty_result = searcher.monetary_value(pl_candidate_sentences)

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
    ll_number_value_result = searcher.after_target_set_number_value(ll_candidate_sentences, ll_stemming_set)
    print(ll_number_value_result)
    print('Candidatos (numéricos) patrimônio líquido:')
    pl_number_value_result = searcher.after_target_set_number_value(pl_candidate_sentences, pl_stemming_set)
    print(pl_number_value_result)
    ph.print_helper.print_line()

    print('Possível valor de ROE')
    roe_indicator = roe.roe()
    possibles_roe = roe_indicator.calculate_iterating(ll_monetary_dirty_result, pl_monetary_dirty_result)
    print(*possibles_roe)
    possibles_roe = roe_indicator.calculate_iterating(ll_monetary_dirty_result, pl_number_value_result)
    print(*possibles_roe)
    possibles_roe = roe_indicator.calculate_iterating(ll_number_value_result, pl_monetary_dirty_result)
    print(*possibles_roe)
    possibles_roe = roe_indicator.calculate_iterating(ll_number_value_result, pl_number_value_result)
    print(*possibles_roe)
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
