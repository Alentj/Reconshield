from urllib.parse import urlparse
import socket
import ssl


def ssl_analyzer(normalized_url):
    parsed_url = urlparse(normalized_url)
    hostname = parsed_url.hostname

    if hostname is None:
        return False, None

    try:
        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

                ssl_info = {
                    "subject": cert.get("subject"),
                    "issuer": cert.get("issuer"),
                    "valid_from": cert.get("notBefore"),
                    "expires_on": cert.get("notAfter"),
                }

                return True, ssl_info

    except (socket.gaierror, socket.timeout, ssl.SSLError):
        return False, None