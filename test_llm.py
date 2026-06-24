from modules.llm_extractor import extract_with_llm

text = """
INVOICE

Invoice Number: 1234567890

Date: 24/06/2026

Total Amount: 4000.00
"""

print(extract_with_llm(text))