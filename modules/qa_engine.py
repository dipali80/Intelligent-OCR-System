from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

def answer_question(document_text, question):

    result = qa_pipeline(
        question=question,
        context=document_text
    )

    return result["answer"]