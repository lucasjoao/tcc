# Import libraries
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# pytesseract.pytesseract.tesseract_cmd = r'/home/lucas/.cache/pypoetry/virtualenvs/tcc-py3.7/bin/pytesseract'

# Store all the pages of the PDF in a variable
pages = convert_from_path('data/weg_2015_1T.pdf', 500)

# Counter to store images of each page of PDF to image
image_counter = 1

# Iterate through all the pages stored above
for page in pages:

    # Declaring filename for each page of PDF as JPG
    # For each page, filename will be:
    # PDF page 1 -> page_1.jpg
    # PDF page 2 -> page_2.jpg
    # PDF page 3 -> page_3.jpg
    # ....
    # PDF page n -> page_n.jpg
    filename = "page_"+str(image_counter)+".jpg"

    # Save the image of the page in system
    page.save(filename, 'JPEG')

    # Increment the counter to update filename
    image_counter = image_counter + 1

'''
Part #2 - Recognizing text from the images using OCR
'''

# Variable to get count of total number of pages
filelimit = image_counter-1
text = ''

# Iterate from 1 to total number of pages
for i in range(1, filelimit + 1):

    # Set filename to recognize text from
    # Again, these files will be:
    # page_1.jpg
    # page_2.jpg
    # ....
    # page_n.jpg
    filename = "page_"+str(i)+".jpg"
    print(filename)

    # Recognize the text as string in image using pytesserct
    text = text + ' ' + str(((pytesseract.image_to_string(Image.open(filename), lang='por'))))

print(text)
