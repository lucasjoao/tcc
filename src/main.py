import PyPDF2
from data_dir_scan import data_dir_scan


files_name = data_dir_scan.get_files_name()
print(len(files_name))

for file_name in files_name:
    pdf_reader = PyPDF2.PdfFileReader(data_dir_scan.get_data_directory() + file_name)

    pdf_text = ''
    for i in range(pdf_reader.numPages):
        pdf_page = pdf_reader.getPage(i)
        pdf_text += pdf_page.extractText()

    print(pdf_text)
    print(pdf_reader.numPages)
