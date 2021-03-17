import nltk
from src.plataform import preprocessor as pp

nltk.download('rslp')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')

preprocessor = pp.preprocessor()
print(preprocessor.execute("Eu gosto de abacate. Também gosto de tangerina."))

