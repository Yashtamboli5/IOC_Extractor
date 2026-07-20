# IOC Extractor (Indicator of Compromise Extractor)

## About the Project

IOC Extractor is a Python command-line tool that extracts Indicators of Compromise (IOCs) from incident report text files.

I created this project as part of my cybersecurity learning journey to improve my Python programming skills and understand how SOC (Security Operations Center) analysts work with incident reports. This project will continue to grow with new features in future phases.

---

## Current Version

**Phase 2 (Completed)**

---

## Features

Currently, the tool can extract:

* IPv4 Addresses
* Email Addresses
* HTTP/HTTPS URLs
* Domain Names
* MD5 Hashes
* SHA1 Hashes
* SHA256 Hashes
* CVE Identifiers

Additional Features:

* Duplicate Removal
* File Validation
* Clean Console Output

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

---

## Project Structure

```text
IOC-Extractor/
│── extractor.py
│── README.md
│── LICENSE
│
├── sample_reports/
│   └── sample_incident.txt
│
├── screenshots/
│   ├── Phase 1 File Is Empty.png
│   ├── Phase 1 File Not Found.png
│   ├── Phase 1 File Path.png
│   ├── Phase 1 OUTPUT.png
│   └── Phase 2 Output.png
│
└── tests/
```

---

## Roadmap

- ✅ Phase 1 Completed
- ✅ Phase 2 Completed
- 🚧 Phase 3 Planned

Upcoming features:

* IPv6 Address Extraction
* MAC Address Extraction
* CSV Export
* JSON Export
* Command-line Arguments
* Support for Multiple Incident Reports
* Threat Intelligence Integration
* VirusTotal API Integration
* AbuseIPDB API Integration
* PDF and DOCX File Support

---

## Learning Objectives

This project helped me practice:

* Python Programming
* Regular Expressions (Regex)
* File Handling
* Modular Programming
* Git & GitHub Workflow
* Cybersecurity Fundamentals

---

## Author

**Developed by Yash Tamboli**

Cybersecurity Student | Python Learner | SOC Enthusiast