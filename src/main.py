import PyPDF2

pdf_file = open('../data/weg_20190724ReleaseResultados2T19.pdf', 'rb')
# TODO: pode gerar resultado melhor
# pdf_file = open('../data/itau_DemonstracoesContabeisCompletas2T2019.pdf', 'rb')
# TODO: precisa ser decriptado
# pdf_file = open('../data/bancointer_itr30062019.pdf', 'rb')
# pdf_file = open('../data/ambev_Q2_2019_Release_Port.pdf', 'rb')
# pdf_file = open('../data/gerdau_rt.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(pdf_file)

pdf_text = ''
for i in range(pdf_reader.numPages):
    pdf_page = pdf_reader.getPage(i)
    pdf_text += pdf_page.extractText()

print(pdf_text)
print(pdf_reader.numPages)
