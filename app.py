

import streamlit as st
from PIL import Image
import os
import json

from modules.preprocessing import preprocess_image
from modules.ocr_engine import extract_text
from modules.classifier import classify_document
from modules.extractor import extract_invoice_data
from modules.llm_extractor import extract_with_llm
from modules.qa_engine import answer_question
from modules.validator import validate_data
from modules.pdf_processor import pdf_to_images

st.set_page_config(
    page_title="Intelligent OCR System",
    page_icon="📄",
    layout="wide"
)

# Session State Initialization
if "processed" not in st.session_state:
    st.session_state["processed"] = False

st.title("📄 Intelligent OCR System")
st.write("Upload a document and extract information using OCR and LLM")

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["jpg", "jpeg", "png", "pdf"]
)

# Upload and OCR
if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Preview
    if uploaded_file.name.lower().endswith(".pdf"):

        st.info("📄 PDF Uploaded Successfully")

    else:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Document",
            use_container_width=True
        )

    if st.button("Run OCR"):

        with st.spinner("Processing Document..."):

            # PDF Processing
            if uploaded_file.name.lower().endswith(".pdf"):

                pdf_pages = pdf_to_images(
                    file_path
                )

                extracted_text = ""

                for page in pdf_pages:

                    processed_image = preprocess_image(
                        page
                    )

                    page_text = extract_text(
                        processed_image
                    )

                    extracted_text += page_text + "\n"

            # Image Processing
            else:

                processed_image = preprocess_image(
                    file_path
                )

                extracted_text = extract_text(
                    processed_image
                )

            document_type = classify_document(
                extracted_text
            )

            json_data = extract_invoice_data(
                extracted_text
            )

            validation_result = validate_data(
                json_data
            )

            llm_output = extract_with_llm(
                extracted_text
            )

            # Save Results
            st.session_state["ocr_text"] = extracted_text
            st.session_state["document_type"] = document_type
            st.session_state["json_data"] = json_data
            st.session_state["validation"] = validation_result
            st.session_state["llm_output"] = llm_output
            st.session_state["processed"] = True

        st.success("Processing Complete")

# Show Results
if st.session_state.get("processed", False):

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📄 Document Type")

        st.info(
            st.session_state["document_type"]
        )

    with col2:

        st.subheader("📊 Extracted JSON")

        st.json(
            st.session_state["json_data"]
        )

        st.download_button(
            label="📥 Download JSON",
            data=json.dumps(
                st.session_state["json_data"],
                indent=4
            ),
            file_name="extracted_data.json",
            mime="application/json"
        )

    st.subheader("✅ Validation Results")

    validation = st.session_state["validation"]

    if validation["document_type"]:
        st.success("Document Type Found")
    else:
        st.error("Document Type Missing")

    if validation["invoice_number"]:
        st.success("Invoice Number Found")
    else:
        st.error("Invoice Number Missing")

    if validation["total_amount"]:
        st.success("Total Amount Found")
    else:
        st.error("Total Amount Missing")

    st.subheader("📝 OCR Output")

    st.text_area(
        "OCR Text",
        st.session_state["ocr_text"],
        height=250
    )

    st.subheader("🤖 LLM Extraction")

    st.text_area(
        "LLM Output",
        st.session_state["llm_output"],
        height=200
    )

    st.subheader("❓ Ask Questions About Document")

    question = st.text_input(
        "Enter your question",
        placeholder="What is the invoice number?",
        key="question_input"
    )

    # No button needed
    if question:

        q = question.lower()

        if "invoice" in q and "number" in q:

            answer = st.session_state[
                "json_data"
            ].get(
                "invoice_number",
                "Not Found"
            )

        elif "total" in q or "amount" in q:

            answer = st.session_state[
                "json_data"
            ].get(
                "total_amount",
                "Not Found"
            )

        elif "document" in q or "type" in q:

            answer = st.session_state[
                "json_data"
            ].get(
                "document_type",
                "Not Found"
            )

        else:

            answer = answer_question(
                st.session_state["ocr_text"],
                question
            )

        st.success(
            f"Answer: {answer}"
        )

