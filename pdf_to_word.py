from pdf2docx import Converter

def pdf_to_word(pdf_file, docx_file):
    # Create a Converter object
    cv = Converter(pdf_file)
    # Convert the PDF to DOCX
    cv.convert(docx_file, start=0, end=None)
    # Close the Converter object
    cv.close()

# Example usage
pdf_file = 'sample.pdf'  # Path to your PDF file
docx_file = 'Output_files/output_word.docx'  # Path to save the DOCX file

pdf_to_word(pdf_file, docx_file)
