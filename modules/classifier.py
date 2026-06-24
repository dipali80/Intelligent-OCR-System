
def classify_document(text):

    text = text.lower()

    if "invoice" in text:
        return "Invoice"

    elif "receipt" in text:
        return "Receipt"

    elif "aadhaar" in text:
        return "Aadhaar"

    elif "permanent account number" in text:
        return "PAN"

    elif "education" in text and "skills" in text:
        return "Resume"

    else:
        return "Unknown"