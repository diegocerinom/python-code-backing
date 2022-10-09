import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((ip_address, port))
    print('server on', (ip_address, port))
    server.listen()
    conn, addr = server.accept()
    with conn:
        print(f'connection by {addr}')
        while True:
            data = conn.recv(1024)
            print('received', data)
            if not data:
                break
            response = 'OK'.encode
        
        print('end')
