import json
from pdf_reader import extract_text_from_pdf
from text_cleaner import clean_text
from extractor import parse_resume

PDF_PATH = "data/sample_resume.pdf"
OUTPUT_PATH = "output/parsed_resume.json"

def main():
    raw_text = extract_text_from_pdf(PDF_PATH)
    cleaned_text = clean_text(raw_text)
    parsed_data = parse_resume(cleaned_text)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(parsed_data, f, indent=4)

    print("Resume parsed successfully!")
    print(parsed_data)

if __name__ == "__main__":
    main()
