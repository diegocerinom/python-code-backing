import socket

host = '127.0.0.1'
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((host, port))
    message = b'message'
    client.sendall(message)
    received = client.recv(1024)

print('received:', repr(received))
