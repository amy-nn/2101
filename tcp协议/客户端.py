import socket
import threading


def msg():
    while True:
        # 3.发消息
        str1 = input(':>')
        client.send(str1.encode())  # 编码
        if str1 == 'byebye':
            client.close()
            break


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2.连接
    client.connect(('127.0.0.1',9008))
    print('连接成功')

    thread_client = threading.Thread(target=msg)
    thread_client.start()

