def risk_engine(vulnerabilities):
    if vulnerabilities is None:
        return False, None

    score = 0

    severity_scores = {
        "Critical": 40,
        "High": 25,
        "Medium": 15,
        "Low": 5
    }

    for vulnerability in vulnerabilities:
        severity = vulnerability.get("severity")
        score += severity_scores.get(severity, 0)

    if score <= 20:
        risk = "Low"
    elif score <= 50:
        risk = "Medium"
    elif score <= 80:
        risk = "High"
    else:
        risk = "Critical"

    report = {
        "score": score,
        "risk": risk,
        "total_vulnerabilities": len(vulnerabilities)
    }

    return True, report