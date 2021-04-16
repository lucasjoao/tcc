import nltk
from src.plataform import preprocessor as pp
from src.technique import stemming as st
from src.plataform import filters as f
from src.plataform import searcher as s

nltk.download('rslp')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')

preprocessor = pp.preprocessor()
stemmer = st.stemming()
filter = f.filters()
searcher = s.searcher()
target_sets = [frozenset([stemmer.stem_word('abacate')])]

text_example = 'Abacate 10 ' \
               'Tangerina 20 ' \
               'Abacate maduro 30'

text_example_preprocessed = preprocessor.execute(text_example)
print(text_example_preprocessed)

text_example_stemmed = stemmer.stem_text_matrix(text_example_preprocessed)
print(text_example_stemmed)

text_example_filtered = filter.candidate_sentences(text_example_stemmed, target_sets)
print(text_example_filtered)

text_example_filtered_in_seq = filter.is_searcher_words_in_sequence(text_example_filtered, target_sets)
print(text_example_filtered_in_seq)

example_monetary_value = searcher.monetary_value(text_example_filtered_in_seq)
print(example_monetary_value)

example_after_target_set = searcher.after_target_set_number_value(text_example_filtered_in_seq, target_sets)
print(example_after_target_set)
