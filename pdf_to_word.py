from pdf2docx import Converter
import fitz  
def pdf_to_word(pdf_file, docx_file):
    # Create a Converter object
    cv = Converter(pdf_file)
    # Convert the PDF to DOCX
    cv.convert(docx_file, start=0, end=None)
    # Close the Converter object
    cv.close()

def pdf_to_text(pdf_file, output_txt_file):
    # Open the PDF file
    document = fitz.open(pdf_file)
    # Initialize a variable to store the extracted text just for checking purpose
    text = ""

    # Loop through each page aafcsa
    for page_num in range(document.page_count):
        page = document[page_num]
        text += page.get_text("text")
    # Save the extracted text to a file
    with open(output_txt_file, 'w', encoding='utf-8') as f:
        f.write(text)

    # Close the PDF document
    document.close()

# Example usage
pdf_file = 'sample.pdf'  # Path to your PDF file
docx_file = 'Output_files/output_word.docx'  # Path to save the DOCX file
text_file = 'Output_files/output_word.txt'
pdf_to_word(pdf_file, docx_file)

pdf_to_text(pdf_file, text_file)
