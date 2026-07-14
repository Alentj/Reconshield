# ReconShield Architecture

## Overview

ReconShield is a modular web security assessment tool.

Each module has a single responsibility and communicates with other modules through well-defined inputs and outputs.

---

## Architecture

User
 │
 ▼
validate_url()
 │
 ▼
normalized_url
 │
 ├──────────────┬──────────────┐
 │              │              │
 ▼              ▼              ▼
dns_resolver()  header_collector()  ssl_analyzer()
 │              │
 ▼              ▼
port_scanner()  security_header_analyzer()
 │
 ▼
service_detector()
 │
 └──────────────┬──────────────┐
                ▼
      vulnerability_engine()
                ▼
         risk_engine()
                ▼
      report_generator()
---

## Module Responsibilities

### URL Validator

Input:
- User URL

Output:
- (True, normalized_url)
- (False, None)

Responsibility:
- Validate and normalize URLs.

---

### DNS Resolver

Input:
- normalized_url

Output:
- (True, ip_address)
- (False, None)

Responsibility:
- Resolve the hostname to an IP address.

---

### Header Collector

Input:
- normalized_url

Output:
- (True, headers)
- (False, None)

Responsibility:
- Collect HTTP response headers.

---

### SSL Analyzer

Input:
- normalized_url

Output:
- SSL information

Responsibility:
- Analyze the website's SSL certificate.

---

### Port Scanner

Input:
- ip_address

Output:
- Open ports

Responsibility:
- Scan common TCP ports.

---

### Service Detector

Input:
- Open ports

Output:
- Detected services

Responsibility:
- Identify services running on open ports.

---

### Security Header Analyzer

Input:
- HTTP headers

Output:
- Missing or insecure security headers

Responsibility:
- Analyze HTTP security headers.

---

### Vulnerability Engine

Input:
- Headers
- SSL Information
- Services

Output:
- Vulnerability findings

Responsibility:
- Match collected information against known vulnerabilities.

---

### Risk Engine

Input:
- All findings

Output:
- Risk score

Responsibility:
- Calculate the overall security risk.

---

### Report Generator

Input:
- Final scan results

Output:
- Human-readable report

Responsibility:
- Generate the final security report.