def validate_data(data):

    validation = {
        "document_type": False,
        "invoice_number": False,
        "total_amount": False
    }

    if data.get("document_type"):
        validation["document_type"] = True

    if data.get("invoice_number"):
        validation["invoice_number"] = True

    if data.get("total_amount"):
        validation["total_amount"] = True

    return validation