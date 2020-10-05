import nltk
from src.indicator import roe as roe
from src.indicator import lucro_liquido as ll
from src.indicator import patrimonio_liquido as pl
from src.plataform import pdf_extract as pe
from src.plataform import preprocessor as pp
from src.plataform import filters as f
from src.plataform import searcher as se
from src.helper import result_helper as rh
from src.technique import stemming as st


class manager:

    def __init__(self, reports_filename):
        nltk.download('rslp')
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('words')

        preprocessor = pp.preprocessor()
        stemming = st.stemming()

        self.lucro_liquido = ll.lucro_liquido()
        self.patrimonio_liquido = pl.patrimonio_liquido()
        self.filters = f.filters()
        self.searcher = se.searcher()

        self.reports_stemming = {}
        for report_filename in reports_filename:
            pdf_text = pe.pdf_extract.get_text(report_filename)
            preprocessed_text = preprocessor.execute(pdf_text)
            self.reports_stemming[report_filename] = stemming.stem_text_matrix(preprocessed_text)

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

    def run_lucro_liquido_monetary(self):
        reports_candidate_sentences = self.__common_process(self.lucro_liquido)

        result = {}
        for filename, candidate_sentences in reports_candidate_sentences.items():
            dirty_result = self.searcher.monetary_value(candidate_sentences)
            result[filename] = rh.result_helper.clean_search_result(dirty_result)
        return result

    def run_lucro_liquido_number(self):
        reports_candidate_sentences = self.__common_process(self.lucro_liquido)

        target_sets = self.lucro_liquido.get_target_sets()

        result = {}
        for filename, candidate_sentences in reports_candidate_sentences.items():
            result[filename] = self.searcher.after_target_set_number_value(candidate_sentences, target_sets)
        return result

    def run_patrimonio_liquido_monetary(self):
        reports_candidate_sentences = self.__common_process(self.patrimonio_liquido)

        result = {}
        for filename, candidate_sentences in reports_candidate_sentences.items():
            dirty_result = self.searcher.monetary_value(candidate_sentences)
            result[filename] = rh.result_helper.clean_search_result(dirty_result)
        return result





