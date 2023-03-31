import socket
import threading
import sys

global halt_flag
halt_flag = False

def connection_thread():
    global halt_flag

    while not halt_flag:
        client, ip = server.accept()
        print(f'已有客户端连入，ip信息是：{ip}')  # ip[0]地址  ip[1]端口号
        thread_server = threading.Thread(target=msg, args=(client, ))
        thread_server.setDaemon(True)
        thread_server.start()
        print("init")

    print("连线线程结束")

def msg(client1):
    while True:
        # 收发消息
        str1 = client1.recv(1024).decode()  # 解码
        print(f"收到:{str1}")

        if str1 and  str1 == 'bye':
            # client1.shutdown(SHUT_RDWR)
            # client1.close()
            # sys.exit(0)
            global  halt_flag
            halt_flag = True
            break

    print("子线程结束")

# 本地：127.0.0.1
if __name__ == '__main__':

    # 1.创建服务器
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket.setdefaulttimeout(3)
    # 2.绑定
    server.bind(('127.0.0.1', 6019))
    # 3.监听
    server.listen(128)
    print('服务器已开启，等待客户端连接。。。')
    # 4.接收客户端  client客户端对象 ip客户端的ip信息

    connection_server = threading.Thread(target=connection_thread)
    connection_server.setDaemon(True)
    connection_server.start()

    import time
    while not halt_flag:
        time.sleep(1)

    print("主线程结束")



