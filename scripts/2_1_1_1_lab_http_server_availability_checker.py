import socket
import sys


# Input:
# 2_1_1_1_lab_http_server_availability_checker.py
# 2_1_1_1_lab_http_server_availability_checker.py onet.pl
# 2_1_1_1_lab_http_server_availability_checker.py onet.pl 80
# 2_1_1_1_lab_http_server_availability_checker.py onet.pl 81
# 2_1_1_1_lab_http_server_availability_checker.py onet.pl -81
# 2_1_1_1_lab_http_server_availability_checker.py onet.pl port

# cmd -> python <file_name> <address> <port=80>


def request(address, port=80):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((address, port))
    except socket.timeout as e:
        print(e)
        sys.exit(3)
    except socket.error as e:
        print(e)
        sys.exit(4)
    else:
        sock.send(
            b"HEAD / HTTP/1.1\r\nHost: "
            + bytes(address, "utf8")
            + b"\r\nConnection: close\r\n\r\n"
        )
        response = sock.recv(
            128
        )  # For best match with hardware and network realities, the value of bufsize should be a relatively small power of 2, for example, 4096.
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return response.splitlines()[0].decode()


if len(sys.argv) not in [2, 3]:
    print(
        """Improper number of arguments: at least one is required and not more than two are allowed:
    - http server's address (required)
    - port number (default to 80 if not specified)"""
    )
    sys.exit(1)
elif len(sys.argv) == 2:
    print(request(sys.argv[1]))
elif len(sys.argv) == 3:
    try:
        server_port = int(sys.argv[2])
        if server_port < 1:
            raise ValueError
    except ValueError:
        print("Port number is invalid - exiting.")
        sys.exit(2)
    else:
        print(request(sys.argv[1], server_port))
