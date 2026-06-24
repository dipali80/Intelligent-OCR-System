import re

def extract_invoice_data(text):

    document_type = "Unknown"

    if "invoice" in text.lower():
        document_type = "Invoice"

    elif "receipt" in text.lower():
        document_type = "Receipt"

    data = {
        "document_type": document_type,
        "invoice_number": None,
        "total_amount": None
    }

    invoice_match = re.search(
        r'(\d{6,})',
        text
    )

    if invoice_match:
        data["invoice_number"] = invoice_match.group()

    amount_match = re.search(
        r'(\d+\.\d{2})',
        text
    )

    if amount_match:
        data["total_amount"] = amount_match.group()

    return data