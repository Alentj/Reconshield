# 🛡️ ReconShield

ReconShield is a modular Python-based web security assessment tool that performs reconnaissance and basic security analysis of websites.

## Features

- URL Validation
- DNS Resolution
- HTTP Header Collection
- SSL Certificate Analysis
- Port Scanning
- Security Header Analysis
- Service Detection
- Vulnerability Detection
- Risk Assessment
- Security Report Generation

## Architecture

(User)
   │
   ▼
URL Validator
   │
   ▼
DNS Resolver
   ├──────────────┐
   ▼              ▼
Port Scanner   Header Collector
                  │
                  ▼
      Security Header Analyzer
                  │
                  ▼
          Vulnerability Engine
                  │
                  ▼
             Risk Engine
                  │
                  ▼
          Report Generator

## Project Structure

```text
ReconShield/
├── recon/
├── tests/
├── docs/
├── main.py
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone <repo-url>
cd ReconShield
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

Example:

```
Enter URL:
https://google.com
```

## Technologies Used

- Python 3
- socket
- ssl
- requests
- urllib.parse

## Future Improvements

- PDF Reports
- CVE Database Integration
- WHOIS Lookup
- DNS Record Analysis
- Web Dashboard
- Multi-threaded Port Scanner

## License

MIT License