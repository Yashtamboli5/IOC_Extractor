import re
import os
import json
import csv
import pdfplumber
from docx import Document

# Get the file path from the user
def get_file_path():
    path = input("Enter the path of the incident report: ").strip()

    # Remove quotes from the file path
    if path.startswith('"') and path.endswith('"'):
        path = path[1:-1]

    return path


# Check if the file is valid
def validate_file(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")

    supported_extensions = (".txt", ".pdf", ".docx", ".csv", ".json", ".log")
    extension = os.path.splitext(path)[1].lower()

    if extension not in supported_extensions:
        raise ValueError(
            f"Unsupported file type: '{extension}'. "
            f"Supported types are: {', '.join(supported_extensions)}"
        )

    # Check if the file is empty
    if os.path.getsize(path) == 0:
        raise ValueError("The file is empty.")

    return path


# Read TXT or LOG file
def _read_txt_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()


# Read CSV file
def _read_csv_file(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore", newline="") as file:
            reader = csv.reader(file)
            rows_as_text = [" ".join(row) for row in reader]
    except csv.Error as error:
        raise ValueError(f"Could not read CSV file: {error}")

    return "\n".join(rows_as_text)


# Read JSON file
def _read_json_file(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as file:
            data = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON file: {error}")

    # Convert JSON to text
    return json.dumps(data, indent=2)


# Read DOCX file
def _read_docx_file(path):
    try:
        document = Document(path)
    except Exception as error:
        raise ValueError(f"Could not read DOCX file: {error}")

    paragraphs = [paragraph.text for paragraph in document.paragraphs]
    return "\n".join(paragraphs)


# Read PDF file
def _read_pdf_file(path):
    page_texts = []

    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()

                # Skip empty pages
                if text:
                    page_texts.append(text)

    except Exception as error:
        raise ValueError(f"Could not read PDF file: {error}")

    return "\n".join(page_texts)


# Read the selected file
def read_file(path):
    extension = os.path.splitext(path)[1].lower()

    if extension in (".txt", ".log"):
        return _read_txt_file(path)

    if extension == ".csv":
        return _read_csv_file(path)

    if extension == ".json":
        return _read_json_file(path)

    if extension == ".docx":
        return _read_docx_file(path)

    if extension == ".pdf":
        return _read_pdf_file(path)

    raise ValueError(f"Unsupported file type: '{extension}'")


# Find IP addresses
def extract_ips(text):
    pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    return sorted(set(re.findall(pattern, text)))


# Find email addresses
def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return sorted(set(re.findall(pattern, text)))


# Find URLs
def extract_urls(text):
    pattern = r"https?://[^\s\"'<>]+"
    return sorted(set(re.findall(pattern, text)))


# Find domains
def extract_domains(text):
    pattern = r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"
    return sorted(set(re.findall(pattern, text)))


# Find MD5 hashes
def extract_md5(text):
    pattern = r"\b[a-fA-F0-9]{32}\b"
    return sorted(set(re.findall(pattern, text)))


# Find SHA1 hashes
def extract_sha1(text):
    pattern = r"\b[a-fA-F0-9]{40}\b"
    return sorted(set(re.findall(pattern, text)))


# Find SHA256 hashes
def extract_sha256(text):
    pattern = r"\b[a-fA-F0-9]{64}\b"
    return sorted(set(re.findall(pattern, text)))


# Find CVE IDs
def extract_cves(text):
    pattern = r"\bCVE-\d{4}-\d{4,7}\b"
    matches = re.findall(pattern, text, re.IGNORECASE)
    return sorted(set(match.upper() for match in matches))


# Print results
def print_section(title, items):
    print(f"\n{title}")
    print("-" * len(title))

    if not items:
        print("None found.")
    else:
        for item in items:
            print(item)


# Main function
def main():
    print("\n===== IOC EXTRACTOR =====")

    file_path = get_file_path()

    try:
        validate_file(file_path)
        data = read_file(file_path)

    except FileNotFoundError as e:
        print(f"\nError: {e}")
        return
    except ValueError as e:
        print(f"\nError: {e}")
        return
    except PermissionError:
        print("\nError: Permission denied.")
        return
    except OSError as e:
        print(f"\nError: {e}")
        return

    print_section("IP Addresses", extract_ips(data))
    print_section("Email Addresses", extract_emails(data))
    print_section("URLs", extract_urls(data))
    print_section("Domains", extract_domains(data))
    print_section("MD5 Hashes", extract_md5(data))
    print_section("SHA1 Hashes", extract_sha1(data))
    print_section("SHA256 Hashes", extract_sha256(data))
    print_section("CVE Identifiers", extract_cves(data))


# Run the program
if __name__ == "__main__":
    main()
