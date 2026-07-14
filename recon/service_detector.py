def service_detector(port_results):
    if port_results is None:
        return False, None

    common_services = {
        20: "FTP-DATA",
        21: "FTP",
        22: "SSH",
        23: "TELNET",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        5432: "PostgreSQL",
        8080: "HTTP-ALT",
    }

    services = {}

    for port, is_open in port_results.items():
        if is_open:
            services[port] = common_services.get(port, "Unknown")

    return True, services