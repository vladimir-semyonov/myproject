from docx import Document

input_file = 'input.txt'
output_file = 'output.docx'


def txt_word(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as txt_file:
        txt = txt_file.read()
    doc = Document()
    doc.add_paragraph(txt)
    doc.save(output_file)

txt_word(input_file, output_file)
