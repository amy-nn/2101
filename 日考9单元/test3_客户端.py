import socket

if __name__ == '__main__':
    while True:
        try:
            client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            ip = input('输入ip地址或主机名')
            client.connect((ip,80))
        except BaseException as e:
            print('非法IP')
        else:
            # 发消息（发给百度）
            client.send(f'GET /+"{ip}"+ HTTP/1.1\r\nHost: www.cip.cc\r\nUser-Agent: curl\r\n\r\n'.encode())
            #收消息（从百度）
            str2 = client.recv(1024).decode()
            print(str2)
