import os.path
import socket
import threading
import time


def msg():
    while True:
        file_name = input('输入上传的文件名:')  #a.txt 文件的名字
        #判断在本地文件夹中是否存在
        if os.path.exists(f'本地/{file_name}'):#本地/a.txt
            #文件名发给服务器，去判断
            client.send(file_name.encode())  #文件名
        else:
            print('本地没有此文件')

        str1 = client.recv(1024).decode()
        print(str1)
        if str1 == '可以上传':
            try:
                start = time.time()
                with open(f'本地/{file_name}','r') as f:
                    str2 = f.read()
                client.send(str2.encode())      #上传
                end = time.time()
                diff = end - start #上传花费的时间
                print(f'本次上传共耗时{diff}秒”')
                file_size = os.path.getsize(f'本地/{file_name}')
                if diff > 0 :
                    speed = file_size/diff  #速度 = 大小/时间
                    print(f'每秒上传的速度是{speed}')
                else:
                    print('花费时间是0秒')
            except BaseException as e:
                print(e)
                print('上传出错')
            else:
                print('上传成功')

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('127.0.0.1',9008))  #假的

    c_thread = threading.Thread(target=msg)
    c_thread.start()
