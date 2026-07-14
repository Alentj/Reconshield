from recon.url_validator import validate_url
from recon.dns_resolver import dns_resolver
from recon.header_collector import header_collector
from recon.ssl_analyzer import ssl_analyzer
from recon.port_scanner import port_scanner
from recon.security_header_analyzer import security_header_analyzer
from recon.service_detector import service_detector
from recon.vulnerability_engine import vulnerability_engine
from recon.risk_engine import risk_engine
from recon.report_generator import report_generator


COMMON_PORTS = [
    21,
    22,
    25,
    53,
    80,
    110,
    143,
    443,
    3306,
    8080,
]


def main():
    url = input("Enter URL: ")

    success, normalized_url = validate_url(url)
    if not success:
        print("Invalid URL")
        return

    success, ip_address = dns_resolver(normalized_url)
    if not success:
        print("DNS resolution failed")
        return

    success, headers = header_collector(normalized_url)
    if not success:
        print("Failed to collect headers")
        return

    success, ssl_info = ssl_analyzer(normalized_url)
    if not success:
        print("SSL analysis failed")
        return

    success, port_results = port_scanner(ip_address, COMMON_PORTS)
    if not success:
        print("Port scan failed")
        return

    success, header_findings = security_header_analyzer(headers)
    if not success:
        print("Header analysis failed")
        return

    success, services = service_detector(port_results)
    if not success:
        print("Service detection failed")
        return

    success, vulnerabilities = vulnerability_engine(
        header_findings,
        ssl_info,
        services,
    )
    if not success:
        print("Vulnerability analysis failed")
        return

    success, risk_report = risk_engine(vulnerabilities)
    if not success:
        print("Risk calculation failed")
        return

    report_generator(
        normalized_url,
        ip_address,
        services,
        header_findings,
        ssl_info,
        vulnerabilities,
        risk_report,
    )


if __name__ == "__main__":
    main()