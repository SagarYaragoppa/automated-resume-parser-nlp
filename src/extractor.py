import re
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python", "java", "c", "c++", "c#", "javascript", "typescript",
    "go", "rust", "php", "ruby", "swift", "kotlin", "r", "matlab",
    "machine learning", "deep learning", "artificial intelligence",
    "nlp", "computer vision", "data science", "data analysis",
    "feature engineering", "model training", "model evaluation",
    "statistical analysis", "tensorflow", "pytorch", "keras", "scikit-learn",
    "xgboost", "lightgbm", "opencv", "nltk", "spacy",
    "hugging face", "transformers","numpy", "pandas", "matplotlib", "seaborn",
    "plotly", "power bi", "tableau", "excel","sql", "mysql", "postgresql", "sqlite",
    "mongodb", "redis", "oracle", "firebase","html", "css", "javascript", "react", "angular", "vue",
    "node.js", "express.js", "django", "flask", "fastapi",
    "rest api", "graphql","git", "github", "gitlab", "docker", "kubernetes",
    "aws", "azure", "google cloud", "ci/cd",
    "linux", "bash", "powershell", "data structures", "algorithms", "object oriented programming",
    "operating systems", "computer networks",
    "database management systems", "software engineering",
    "system design"
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
