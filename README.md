# IOC Extractor (Indicator of Compromise Extractor)

## About the Project

IOC Extractor is a Python command-line tool that extracts Indicators of Compromise (IOCs) from incident report text files.

I created this project as part of my cybersecurity learning journey to improve my Python programming skills and understand how SOC (Security Operations Center) analysts work with incident reports. This project will continue to grow with new features in future phases.

---

## Phase 1 Features

Currently, the tool can extract:

* IPv4 Addresses
* Email Addresses
* HTTP/HTTPS URLs

---

## Technologies Used

* Python 3
* Regular Expressions (Regex)
* File Handling
* Standard Python Libraries (`re`, `os`)

---

## How to Run

Run the program using:

```bash
python extractor.py
```

The program will ask you to enter the full path of the incident report.

Example:

```text
Enter the path of the incident report:
C:\Users\Yash\Documents\incident.txt
```

The incident report can be stored anywhere on your computer. The program reads the file directly from the path you provide.

---

## Example Output

```text
====================================
IOC EXTRACTOR
====================================

IP Addresses
-------------------
192.168.1.10
8.8.8.8

Email Addresses
-------------------
admin@example.com
support@test.com

URLs
-------------------
http://example.com/login
https://google.com
```

---

## Project Structure

```text
IOC-Extractor/
│── extractor.py
│── README.md
```

---

## Future Improvements

This project is being developed step by step. In the upcoming phases, I plan to add:

* Domain Name Extraction
* MD5, SHA1 and SHA256 Hash Extraction
* CSV and JSON Export
* Command-line Arguments
* Support for Multiple Incident Reports
* Threat Intelligence Integration
* VirusTotal API Integration
* AbuseIPDB API Integration
* PDF and DOCX File Support

---

## Author

Developed by **Yash Tamboli**

Cybersecurity Student | Python Learner | SOC Enthusiast
