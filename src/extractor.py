import re
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python", "java", "c++", "machine learning",
    "deep learning", "nlp", "sql", "tensorflow", "pytorch"
]

def extract_name(text: str):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_email(text: str):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None

def extract_skills(text: str):
    text = text.lower()
    return list({skill for skill in SKILLS if skill in text})

def parse_resume(text: str) -> dict:
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "skills": extract_skills(text)
    }
