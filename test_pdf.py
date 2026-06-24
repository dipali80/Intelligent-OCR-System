from pdf2image import convert_from_path

pages = convert_from_path(
    "uploads/dummy_statement_pdf.pdf"
)

print("Pages Found:", len(pages))