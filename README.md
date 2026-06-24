📄 Intelligent OCR System with Open-Source LLM Integration
📖 Introduction

The Intelligent OCR System is an AI-powered document processing application designed to extract, analyze, validate, and understand information from images and PDF documents.

The system combines Computer Vision, OCR, Natural Language Processing (NLP), and Open-Source Large Language Models (LLMs) to automate document understanding and information extraction.

Using OpenCV, EasyOCR, FLAN-T5, and DistilBERT, the application can process invoices, receipts, and PDF documents while providing structured JSON outputs and an interactive question-answering interface.

The project demonstrates an end-to-end Intelligent Document Processing (IDP) workflow suitable for real-world document automation scenarios.


🎯 Project Objectives
Extract text from images and PDF documents.
Improve OCR accuracy through image preprocessing.
Classify uploaded documents.
Extract structured information from OCR text.
Validate extracted information.
Integrate an open-source LLM for intelligent document understanding.
Allow users to interact with documents using natural language questions.
Export extracted information in JSON format.


🌟 Key Features

✅ Image OCR (JPG, PNG, JPEG)

✅ Multi-Page PDF OCR Support

✅ OpenCV-Based Image Preprocessing

✅ EasyOCR Text Recognition

✅ Document Classification

✅ Information Extraction

✅ Data Validation

✅ Open-Source LLM Integration (FLAN-T5)

✅ DistilBERT-Based Question Answering

✅ JSON Output Generation

✅ Downloadable Results

✅ Interactive Streamlit User Interface

💼 Use Cases
Invoice Processing
Extract invoice numbers
Extract total amounts
Identify document type
Generate structured JSON data
Receipt Processing
Extract transaction details
Process scanned receipts
Organize receipt information
PDF Document Processing
Process multi-page PDF files
Extract text from scanned documents
Analyze document content
Intelligent Question Answering

Users can ask questions such as:

What is the invoice number?
What is the total amount?
What is the document type?
What information is present in the document?
Business Automation
Reduce manual data entry
Improve document processing efficiency
Automate information extraction workflows




workflows
🛠️ Technologies Used
Technology	Purpose
Python	Core Programming Language
Streamlit	Web Application Framework
OpenCV	Image Processing
EasyOCR	Optical Character Recognition
FLAN-T5	Open-Source LLM
DistilBERT	Question Answering
Transformers	NLP Framework
PDF2Image	PDF Processing
Pillow	Image Handling
JSON	Structured Data Output
💻 System Requirements
Hardware Requirements
Processor: Intel i3 or above
RAM: 4 GB minimum (8 GB recommended)
Storage: 2 GB free space
Software Requirements
Python 3.10+
Git
Poppler (for PDF support)
Operating System
Windows 10/11
Linux
macOS
⚙️ Project Setup
Clone Repository
git clone https://github.com/your-username/Intelligent_OCR_System.git
cd Intelligent_OCR_System
Create Virtual Environment
python -m venv myenv
Activate Environment

Windows:

myenv\Scripts\activate

Linux/macOS:

source myenv/bin/activate
Install Dependencies
pip install -r requirements.txt
📦 Required Libraries
streamlit
easyocr
opencv-python
pillow
transformers
torch
pdf2image
numpy
▶️ Running the Application
streamlit run app.py

After running the command:

Open browser:

http://localhost:8501



📋 How to Use
Step 1

Launch the application.

Step 2

Upload a document:

JPG
JPEG
PNG
PDF
Step 3

Click:

Run OCR

Step 4

Wait for processing to complete.

Step 5

View:

Document Type
Extracted JSON
Validation Results
OCR Text
LLM Output
Step 6

Ask questions about the uploaded document.

Examples:

What is the invoice number?
What is the total amount?
What is the document type?
Step 7

Download the extracted JSON file.

🏗️ System Architecture

Document Upload
↓
Image/PDF Processing
↓
OpenCV Preprocessing
↓
EasyOCR Extraction
↓
Document Classification
↓
Information Extraction
↓
Validation
↓
FLAN-T5 Processing
↓
JSON Output
↓
Question Answering



🔍 OCR Workflow
Upload Document
Image Preprocessing
OCR Extraction
Text Aggregation
Document Classification
Information Extraction
Validation
JSON Generation
Question Answering
🤖 LLM Integration

The project integrates Google's FLAN-T5 open-source model.

The LLM is used to:

Understand extracted OCR text
Improve information extraction
Generate meaningful document insights
Support intelligent processing

No proprietary APIs such as OpenAI, Gemini, Claude, or paid OCR services are used.

❓ Question Answering Module

The system includes a DistilBERT-based Question Answering module.

Users can interact with documents using natural language queries.

Example:

Question:
What is the invoice number?

Answer:
1234567890

The QA module uses OCR-extracted text as contextual information.

✅ Validation Logic

The validation module checks:

Document Type Availability
Invoice Number Availability
Total Amount Availability

Validation results are displayed to users in real time.


🚀 Future Improvements
Multi-Language OCR Support
Advanced Information Extraction
Cloud Deployment
Database Integration
Better Open-Source LLM Models
Additional Document Type Support
👩‍💻 Author

Dipali Hambarde
