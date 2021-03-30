import nltk
from src.plataform import preprocessor as pp
from src.technique import stemming as st

nltk.download('rslp')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')

preprocessor = pp.preprocessor()
stemmer = st.stemming()

text_example = "Eu gosto de abacate. Também gosto de tangerina."

text_example_preprocessed = preprocessor.execute(text_example)
print(text_example_preprocessed)
print(stemmer.stem_text_matrix(text_example_preprocessed))
