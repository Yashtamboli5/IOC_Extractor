# IOC Extractor (Indicator of Compromise Extractor)

## About the Project

IOC Extractor is a Python command-line tool that extracts Indicators of Compromise (IOCs) from incident reports.

The tool supports multiple file formats and automatically extracts common cybersecurity indicators such as IP addresses, email addresses, URLs, domain names, file hashes, and CVE identifiers.

I built this project as part of my cybersecurity learning journey to improve my Python programming skills, work with Regular Expressions (Regex), and understand how Security Operations Center (SOC) analysts investigate incident reports.

---

## Current Version

**Phase 3 (Completed)**

---

## Features

The tool can extract the following Indicators of Compromise (IOCs):

- IPv4 Addresses
- Email Addresses
- HTTP/HTTPS URLs
- Domain Names
- MD5 Hashes
- SHA1 Hashes
- SHA256 Hashes
- CVE Identifiers

Additional Features:

- Support for multiple file formats
- Duplicate removal
- File validation
- Error handling
- Clean console output

---

## Supported File Formats

The program supports the following file formats:

- TXT
- PDF
- DOCX
- CSV
- JSON
- LOG

---

## Technologies Used

- Python 3
- Regular Expressions (Regex)
- File Handling
- JSON
- CSV
- pdfplumber
- python-docx

Python Libraries:

- re
- os
- json
- csv
- pdfplumber
- python-docx

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Yashtamboli5/IOC_Extractor.git
```

Go to the project folder:

```bash
cd IOC_Extractor
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install pdfplumber python-docx
```

---

## How to Run

Run the program:

```bash
python extractor.py
```

The program will ask you to enter the full path of the incident report.

Example:

```text
Enter the path of the incident report:

C:\Users\Yash\Documents\incident.pdf
```

Supported file formats:

- TXT
- PDF
- DOCX
- CSV
- JSON
- LOG

---

## Example Output

```text
===== IOC EXTRACTOR =====

IP Addresses
------------
192.168.1.10
8.8.8.8

Email Addresses
---------------
admin@example.com
support@test.com

URLs
----
http://example.com/login
https://google.com

Domains
-------
example.com
google.com

MD5 Hashes
----------
44d88612fea8a8f36de82e1278abb02f

SHA1 Hashes
-----------
3395856ce81f2b7382dee72602f798b642f14140

SHA256 Hashes
-------------
275a021bbfb6488f4d0b4d6f0f6ef0b4f95fbe4d6dfeff2a7d9e3d8efc9c4d7e

CVE Identifiers
---------------
CVE-2025-12345
```

---

## Screenshots

### Phase 1 Output

![Phase 1 Output](screenshots/Phase%201%20OUTPUT.png)

### Phase 2 Output

![Phase 2 Output](screenshots/Phase%202%20Output.png)

### Phase 3 Output

![Phase 3 Output](screenshots/Phase%203%20.CSV_File%20OUPUT.png)

---

## Project Structure

```text
IOC_Extractor/
│
├── extractor.py
├── README.md
├── requirements.txt
├── LICENSE.txt
│
├── sample_reports/
│   ├── Incident_Report_1.docx
│   ├── Incident_Report_2.pdf
│   ├── Incident_Report_3.json
│   ├── Incident_Report_4.csv
│   └── Incident_Report_5.log
│
├── screenshots/
│   ├── Phase 1 File Is Empty.png
│   ├── Phase 1 File Not Found.png
│   ├── Phase 1 File Path.png
│   ├── Phase 1 OUTPUT.png
│   ├── Phase 2 Output.png
│   └── Phase 3 .CSV_File OUPUT.png
│
└── tests/
```

---

## Roadmap

- ✅ Phase 1 Completed
- ✅ Phase 2 Completed
- ✅ Phase 3 Completed
- 🚧 Phase 4 Planned

Planned Features:

- IPv6 Address Extraction
- MAC Address Extraction
- Export Results to CSV
- Export Results to JSON
- Command-line Arguments
- Scan Multiple Files
- VirusTotal API Integration
- AbuseIPDB API Integration

---

## Learning Objectives

This project helped me practice:

- Python Programming
- Regular Expressions (Regex)
- File Handling
- Reading PDF files
- Reading DOCX files
- Reading CSV files
- Reading JSON files
- Error Handling
- Modular Programming
- Git & GitHub Workflow
- Cybersecurity Fundamentals

---

## Requirements

Python 3.10 or later

Required packages:

- pdfplumber
- python-docx

Install them using:

```bash
pip install -r requirements.txt
```

---

## Author

**Developed by Yash Tamboli**

Cybersecurity Student | Python Learner | SOC Enthusiast

---

## License

This project is licensed under the MIT License.

See the LICENSE.txt file for more information.