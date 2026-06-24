
from modules.preprocessing import preprocess_image
from modules.ocr_engine import extract_text
from modules.classifier import classify_document
from modules.extractor import extract_invoice_data

image_path = "C:/Users/HP/OneDrive/Desktop/Intelligent_OCR_System/sample_documents/invoice.png"


processed_image = preprocess_image(image_path)

text = extract_text(processed_image)

print("\n===== EXTRACTED TEXT =====\n")
print(text)

document_type = classify_document(text)

print("\n===== DOCUMENT TYPE =====\n")
print(document_type)

json_data = extract_invoice_data(text)

print("\n===== JSON OUTPUT =====\n")
print(json_data)




# for the question answering


from modules.qa_engine import answer_question

question = "What is the invoice number?"

answer = answer_question(
    text,
    question
)

print("\n===== QUESTION =====")
print(question)

print("\n===== ANSWER =====")
print(answer)

