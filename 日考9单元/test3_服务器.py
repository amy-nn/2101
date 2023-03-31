import socket

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('127.0.0.1',9090))
    server.listen(5)
    while True:
        client,ip = server.accept()
        while True:
            str1 = client.recv(1024).decode()
            print(str1)