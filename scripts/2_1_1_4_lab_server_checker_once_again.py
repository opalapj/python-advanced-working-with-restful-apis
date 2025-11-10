import sys

import requests


# Input:
# 2_1_1_1_lab_http_server_availability_checker.py
# 2_1_1_1_lab_http_server_availability_checker.py onet.pl
# 2_1_1_1_lab_http_server_availability_checker.py onet.pl 80
# 2_1_1_1_lab_http_server_availability_checker.py onet.pl 81
# 2_1_1_1_lab_http_server_availability_checker.py onet.pl -81
# 2_1_1_1_lab_http_server_availability_checker.py onet.pl port

# cmd -> python <file_name> <address> <port=80>


def request(address, port=80):
    uri = "http://{}:{}".format(address, port)
    try:
        response = requests.head(uri)
    except requests.Timeout as exc:
        print(exc)
        sys.exit(3)
    except requests.RequestException as exc:
        print(exc)
        sys.exit(4)
    else:
        return response.status_code


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
