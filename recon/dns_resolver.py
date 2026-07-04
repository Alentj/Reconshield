"""
Project: ReconShield

Module:
DNS Resolver

Responsibility:
The DNS Resolver is responsible for converting a validated website URL
into its IP address using DNS lookup.

Author:
Alen Joy

TODO:
- Extract hostname
- Perform DNS lookup
- Handle invalid domains

What I Learn:

Why every module should have one responsibility.
- Why urlparse() is better than manual string manipulation.
"""

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