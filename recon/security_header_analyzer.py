def security_header_analyzer(headers):
    required_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]

    findings = {}

    if headers is None:
        return False, None

    for header in required_headers:
        findings[header] = header in headers

    return True, findings