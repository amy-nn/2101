import os.path
import socket
import threading

def msg(client):
    while True:
        f_name = client.recv(1024).decode()  #文件名
        if f_name:  #如何收到的文件名不为空
            print(f_name) #文件名
            #1.判断服务器中是否有这个文件，如果有告诉客户端已存在
            if os.path.exists(f'云服务器/{f_name}'):
                client.send('服务器已存在这个文件了'.encode())
            else:
                client.send('可以上传'.encode())
                str2 = client.recv(1024*40).decode()  #内容
                with open(f'云服务器/{f_name}','w') as f:
                    f.write(str2)

if __name__ == '__main__':

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('127.0.0.1',9008))
    server.listen(5)  #最大连接数
    while True:
        client,ip = server.accept()
        print(ip)

        s_thread = threading.Thread(target=msg,args=(client,))
        s_thread.start()

