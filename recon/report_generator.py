def report_generator(
    normalized_url,
    ip_address,
    services,
    header_findings,
    ssl_info,
    vulnerabilities,
    risk_report,
):
    print("\n" + "=" * 50)
    print("        ReconShield Security Report")
    print("=" * 50)

    print(f"\nTarget URL : {normalized_url}")
    print(f"IP Address : {ip_address}")

    print("\nOpen Services")
    print("-" * 50)
    if services:
        for port, service in services.items():
            print(f"{port:<6} {service}")
    else:
        print("No open services found.")

    print("\nSecurity Headers")
    print("-" * 50)
    for header, present in header_findings.items():
        status = "✓" if present else "✗"
        print(f"{status} {header}")

    print("\nSSL Certificate")
    print("-" * 50)
    print(f"Issuer      : {ssl_info.get('issuer')}")
    print(f"Subject     : {ssl_info.get('subject')}")
    print(f"Valid From  : {ssl_info.get('valid_from')}")
    print(f"Expires On  : {ssl_info.get('expires_on')}")

    print("\nVulnerabilities")
    print("-" * 50)

    if vulnerabilities:
        for vulnerability in vulnerabilities:
            print(f"[{vulnerability['severity']}] {vulnerability['issue']}")
            print(f"Recommendation: {vulnerability['recommendation']}")
            print()
    else:
        print("No vulnerabilities found.")

    print("Risk Summary")
    print("-" * 50)
    print(f"Risk Score : {risk_report['score']}")
    print(f"Risk Level : {risk_report['risk']}")
    print(
        f"Total Findings : {risk_report['total_vulnerabilities']}"
    )

    print("=" * 50)