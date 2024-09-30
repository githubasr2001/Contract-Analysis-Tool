import os
import pdfplumber
import pytesseract
from PIL import Image
import docx
import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + '\n'
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text

def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def analyze_document(file_path):
    file_extension = os.path.splitext(file_path)[-1].lower()
    text = ''

    if file_extension == '.pdf':
        text = extract_text_from_pdf(file_path)
    elif file_extension in ['.docx', '.doc']:
        text = extract_text_from_docx(file_path)
    elif file_extension in ['.jpg', '.jpeg', '.png']:
        text = extract_text_from_image(file_path)
    else:
        raise ValueError("Unsupported file type: {}".format(file_extension))

    # Process the extracted text with spaCy
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = []
        entities[ent.label_].append(ent.text)

    return entities
