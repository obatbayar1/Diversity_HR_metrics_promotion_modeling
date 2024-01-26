pip install pdfminer.six

import os
from pdfminer.high_level import extract_text
import re

def extract_text_from_pdf(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

def parse_cv_sections(text):
    sections = ['Publications', 'Education', 'Experience', 'Awards', 'Conferences']
    section_content = {section: [] for section in sections}
    current_section = None

    lines = text.split('\n')
    for line in lines:
        if any(section in line for section in sections):
            current_section = [section for section in sections if section in line][0]
        elif current_section:
            section_content[current_section].append(line)
    
    return section_content

def process_single_cv(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    if text:
        return parse_cv_sections(text)
    return None

def batch_process_cvs(cv_directory):
    all_cv_data = {}
    for filename in os.listdir(cv_directory):
        if filename.endswith('.pdf'):
            path = os.path.join(cv_directory, filename)
            try:
                cv_data = process_single_cv(path)
                if cv_data:
                    all_cv_data[filename] = cv_data
            except Exception as e:
                print(f"Failed to process {filename}: {e}")
    
    return all_cv_data

def main():
    cv_directory = 'path_to_cv_directory'  # Replace with the actual directory path
    cv_data = batch_process_cvs(cv_directory)
    for filename, content in cv_data.items():
        print(f"Processed CV: {filename}")
        for section, text in content.items():
            print(f"Section: {section}\n{' '.join(text)}\n")

if __name__ == '__main__':
    main()

