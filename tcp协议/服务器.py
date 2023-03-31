import socket
import threading
from _socket import SHUT_RDWR

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('127.0.0.1',9008))
    server.listen(5)

    while True:
        client,ip = server.accept()  #收多个客户端
        flag = 0

        while True:
            str1 = client.recv(1024).decode()  #多收消息
            print(str1)
            with open('服务器聊天记录.txt','a') as f:
                f.write(f'{str1}\n')
            if str1 == 'byebye':
                flag = 1
                break
        # if flag == 1:
        #     break


















