import socket


def port_scanner(ip_address, ports):
    results = {}

    try:
        for port in ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)

                result = sock.connect_ex((ip_address, port))

                if result == 0:
                    results[port] = True
                else:
                    results[port] = False

        return True, results

    except socket.error:
        return False, None