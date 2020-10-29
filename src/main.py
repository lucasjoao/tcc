# Import libraries
import pytesseract
from pdf2image import convert_from_path

pages = convert_from_path('data/weg_2015_1T.pdf', 500)
text = ''

for page in pages:
    text = text + ' ' + pytesseract.image_to_string(page, lang='por')

print(text)
