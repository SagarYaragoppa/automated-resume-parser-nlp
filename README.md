# 📄 Resume Parser Using NLP

## 🔍 Project Overview

This project implements an **NLP-based Resume Parsing System** that automatically extracts structured information from unstructured resumes (PDF or text format).
The system uses a **fine-tuned pretrained Named Entity Recognition (NER) model** along with **rule-based NLP techniques** to accurately identify key resume details.

The final output is stored in a clean **JSON format**, making it suitable for integration with Applicant Tracking Systems (ATS) or HR analytics pipelines.

---

## 🎯 Key Objectives

* Convert unstructured resume text into structured data
* Extract key information such as:

  * Name
  * Contact details
  * Skills
  * Education
  * Experience
* Improve extraction accuracy using **custom rules and fine-tuned NER**

---

## 🧠 Approach & Methodology

The system follows a **hybrid NLP pipeline**:

1. **Resume Input**
   Accepts resumes in PDF or TXT format.

2. **Text Extraction**
   Extracts raw text from PDF resumes using PDF parsing libraries.

3. **Text Preprocessing**
   Cleans and normalizes text for better NLP performance.

4. **Named Entity Recognition (NER)**
   Uses a **pretrained spaCy NER model**, fine-tuned on resume-specific data to identify entities such as:

   * PERSON
   * ORGANIZATION
   * DATE
   * SKILL
   * DEGREE

5. **Rule-Based Extraction**
   Applies regular expressions and keyword-based rules to extract:

   * Email address
   * Phone number
   * Skills and section-specific data

6. **Entity Normalization & Validation**
   Removes duplicates and standardizes extracted entities.

7. **Structured Output Generation**
   Stores extracted information in structured **JSON format**.

---

## 🏗️ Project Architecture

```
resume-parser/
│
├── data/
│   ├── resumes/           # Input resume files
│   └── annotations/       # Labeled training data for NER
│
├── models/
│   └── ner_model/         # Fine-tuned spaCy NER model
│
├── src/
│   ├── pdf_extractor.py   # PDF to text extraction
│   ├── preprocess.py      # Text cleaning & normalization
│   ├── ner.py             # NER inference logic
│   ├── rules.py           # Regex & rule-based extraction
│   └── parser.py          # End-to-end pipeline
│
├── output/
│   └── parsed_resume.json # Final structured output
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

* **Python**
* **spaCy (NLP & NER)**
* **NLTK (optional preprocessing)**
* **PyPDF2 / pdfplumber**
* **Regular Expressions (Regex)**
* **JSON**

---

## 🤖 Model Details

* **Base Model:** spaCy pretrained English NER model
* **Enhancement:** Fine-tuned on resume-specific annotated data
* **Training Type:** Transfer learning (no training from scratch)

This approach ensures:

* Faster development
* Better accuracy with limited data
* Industry-aligned ML practices

---

## 📤 Sample Output

```json
{
  "name": "Rahul Sharma",
  "email": "rahul.sharma@gmail.com",
  "phone": "9876543210",
  "skills": ["Python", "Machine Learning", "NLP", "SQL"],
  "education": [
    "B.Tech in Computer Science, XYZ University (2019–2023)"
  ],
  "experience": [
    "AI Intern - Infosys (Jan 2023 – Jun 2023)"
  ]
}
```

---

## 🚀 How to Run the Project

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run parser
python src/parser.py
```

---

## 📈 Results & Accuracy

* Improved entity extraction accuracy using custom rules
* Reduced false positives compared to raw NER output
* Successfully parsed resumes with varied formats

---

## 🔮 Future Enhancements

* Resume–job description matching
* Skill gap analysis
* Streamlit-based UI
* Multilingual resume support
* Integration with GenAI for resume summarization

---

## 👤 Author

**Sagar Yaragoppa**
B.Tech AIML Student
Project built as a continuation of Neural Network fundamentals and applied NLP learning.

