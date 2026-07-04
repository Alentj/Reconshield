from urllib.parse import urlparse
import socket
def dns_resolver(normalized_url):
   
    parsed_url = urlparse(normalized_url)
    hostname = parsed_url.hostname
    if hostname is None:
        return False, None

    try:
        ip_address = socket.gethostbyname(hostname)
        return  True,ip_address
    except socket.gaierror:
        return False,None