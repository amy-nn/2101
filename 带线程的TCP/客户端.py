import os.path
import random
import socket
import string
import threading
import time


# 客户端
# 1)客户端可以将本地文件上传到服务端，若文件存在上传，若不存在则提示不存在
# 2)上传完后要打印 “本次上传共耗时xx秒”，
# 3)同时打印出上传速度，根据上传时间和文件大小计算每秒上传速度
# 4)客户端要无限循环可以接收来自用户的输入，不能只上传一次就结束程序
# 5)程序需要有必要的异常处理
#多线程的聊天  exit bye
def msg():
    # 多发多收
    while True:
        nums = ''.join(random.choices(string.digits,k=6))
        client.send(nums.encode())
        time.sleep(10)

    client.close()  #客户端关闭


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client.connect(('www.baidu.com',8888))
    except BaseException as e:
        print('服务器地址有错，连接不上')

    thread1 = threading.Thread(target=msg)  #子线程
    thread1.start()


