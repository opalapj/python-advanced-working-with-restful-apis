import socket


HOSTNAME = "www.python.org"
PORT = 80  # Port 80 is the port number assigned to commonly used internet communication protocol, Hypertext Transfer Protocol (HTTP).
BUFFER = 1024
with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as socket_:
    socket_.connect((HOSTNAME, PORT))
    socket_.send(
        b"GET / HTTP/1.1\r\n"
        b"Host: " + bytes(HOSTNAME, "utf8") + b"\r\n"
        b"Connection: close\r\n"
        b"\r\n"
    )
    response = socket_.recv(BUFFER)
    socket_.shutdown(socket.SHUT_RDWR)
print(response.decode())
