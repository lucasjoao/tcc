import nltk
from src.indicator import roe as roe
from src.indicator import lucro_liquido as ll
from src.indicator import patrimonio_liquido as pl
from src.plataform import pdf_extract as pe
from src.plataform import preprocessor as pp
from src.plataform import filters as f
from src.plataform import searcher as se
from src.helper import result_helper as rh
from src.helper import list_helper as lh
from src.technique import stemming as st


class manager:

    def __init__(self, reports_filename, text_extract_lib='pypdf2', custom_config_extract_lib=' '):
        nltk.download('rslp')
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('words')

        preprocessor = pp.preprocessor()
        stemming = st.stemming()

        self.lucro_liquido = ll.lucro_liquido()
        self.patrimonio_liquido = pl.patrimonio_liquido()
        self.roe = roe.roe()

        self.filters = f.filters()
        self.searcher = se.searcher()

        self.reports_stemming = {}
        for report_filename in reports_filename:
            pdf_text = self.__get_pdf_text(report_filename, text_extract_lib, custom_config_extract_lib)
            preprocessed_text = preprocessor.execute(pdf_text)
            self.reports_stemming[report_filename] = stemming.stem_text_matrix(preprocessed_text)

    def __get_pdf_text(self, report_filename, text_extract_lib, custom_config_extract_lib):
        pdf_text = ''
        if text_extract_lib == 'pypdf2':
            pdf_text = pe.pdf_extract.get_text_pypdf2(report_filename)
        elif text_extract_lib == 'pytesseract':
            pdf_text = pe.pdf_extract.get_text_pytesseract(report_filename, custom_config_extract_lib)
        return pdf_text

    def __common_process(self, indicator):
        target_sets = indicator.get_target_sets()

        result = {}
        for filename, stem_text_matrix in self.reports_stemming.items():
            candidate_sentences = self.filters.candidate_sentences(stem_text_matrix, target_sets)
            false_candidate_sentences = self.filters.candidate_sentences(candidate_sentences, indicator.get_filter_sets())
            candidate_sentences = [sentence for sentence in candidate_sentences if sentence not in false_candidate_sentences]
            candidate_sentences = self.filters.is_searcher_words_in_sequence(candidate_sentences, target_sets)
            result[filename] = candidate_sentences
        return result

    def __common_process_monetary(self, indicator):
        reports_candidate_sentences = self.__common_process(indicator)

        result = {}
        for filename, candidate_sentences in reports_candidate_sentences.items():
            dirty_result = self.searcher.monetary_value(candidate_sentences)
            result_with_duplicate = rh.result_helper.clean_search_result(dirty_result)
            result[filename] = lh.list_helper.remove_duplicates_list_of_dicts(result_with_duplicate)
        return result

    def __common_process_number(self, indicator):
        reports_candidate_sentences = self.__common_process(indicator)

        target_sets = indicator.get_target_sets()

        result = {}
        for filename, candidate_sentences in reports_candidate_sentences.items():
            result_with_duplicate = self.searcher.after_target_set_number_value(candidate_sentences, target_sets)
            result[filename] = lh.list_helper.remove_duplicates_list_of_dicts(result_with_duplicate)
        return result

    def run_lucro_liquido_monetary(self):
        return self.__common_process_monetary(self.lucro_liquido)

    def run_lucro_liquido_number(self):
        return self.__common_process_number(self.lucro_liquido)

    def run_patrimonio_liquido_monetary(self):
        return self.__common_process_monetary(self.patrimonio_liquido)

    def run_patrimonio_liquido_number(self):
        return self.__common_process_number(self.patrimonio_liquido)

    def run_roe_monetary(self):
        return self.__common_process_monetary(self.roe)

    def run_roe_number(self):
        return self.__common_process_number(self.roe)

    def run_calculate_roe(self):
        lucro_liquido_number = self.run_lucro_liquido_number()
        lucro_liquido_monetary = self.run_lucro_liquido_monetary()
        patrimonio_liquido_number = self.run_patrimonio_liquido_number()
        patrimonio_liquido_monetary = self.run_patrimonio_liquido_monetary()

        result = {}
        for filename in self.reports_stemming.keys():
            result_file = []
            result_file += self.roe.calculate_iterating(lucro_liquido_number[filename], patrimonio_liquido_number[filename])
            result_file += self.roe.calculate_iterating(lucro_liquido_number[filename], patrimonio_liquido_monetary[filename])
            result_file += self.roe.calculate_iterating(lucro_liquido_monetary[filename], patrimonio_liquido_number[filename])
            result_file += self.roe.calculate_iterating(lucro_liquido_monetary[filename],
                                                        patrimonio_liquido_monetary[filename])
            result[filename] = result_file
        return result
