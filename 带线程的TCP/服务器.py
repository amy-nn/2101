import os.path
import random
import socket
import string
import threading

# TCP是通信协议(打电话） UDP（发短信） （手机打电话 ，微信，QQ...)
# 实现一个简单的TCP文件上传程序，包括客户端与服务端，客户端可以上传指定文件到服务端 （50分）
# 具体要求
# 服务端
# 1)服务端必须无限循环并保持一直运行
# 2)客户端连接到服务端后，服务端需要打印客户端地址和端口号
# 3)服务端接收客户端发送的文件，将文件存储在当前目录下
# 4)服务端先根据文件名检测当前目录下是否已存在同名文件，如果存在则返回给客户端错误提示
def msg(client):
    # 多 收多发
    while True:
        # 收消息
        str1 = client.recv(1024).decode()
        print(str1)

        with open('server.log','a') as f:
            f.write(f'{str1}')



    client.close()  #客户端关闭

if __name__ == '__main__':

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8888))
    server.listen(5)
    print('服务器已开启。。。')

    while True:
        client, ip = server.accept()  # 多收客户端
        print(ip)  # 客户端的ip[0]  ip[1]
        thread1 = threading.Thread(target=msg, args=(client,))
        thread1.start()

        #缺服务器的关闭









