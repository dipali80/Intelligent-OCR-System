
from transformers import pipeline

llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

def extract_with_llm(text):

    prompt = f"""
Extract information from this document.

Return in this format:

Document Type:
Invoice Number:
Date:
Total Amount:

Document:

{text}
"""

    result = llm(
        prompt,
        max_new_tokens=100,
        do_sample=False
    )

    return result[0]["generated_text"]