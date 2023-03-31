# 使用多线程编程完成一个端口扫描程序（20分）
# 1.	把219.28.22.100到219.28.22.105  5台主机的1到100端口存放到一个队列中。
# 2.	开启20个线程，每次从队列中拿出一组ip和端口进行处理
# 3.	处理时首先对端口进行tcp连接，如果连接报异常则为不可连通，记录下ip和端口，连接成功则关闭tcp连接。
# 4.	当队列为空时，线程自动退出。
# 5.	最终打印所有连接失败的ip和端口。
import socket
import threading
from queue import Queue


def test_path():
    for i in range(25):  #从队列拿出25个  （500/20)
        ip_info = que.get()  # ('219.28.22.100', 1)元组
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ip_info)
        except BaseException as e:
            print(f'ip：{ip_info[0]},端口号：{ip_info[1]}测试不通过')
        else:
            print('通过 ')
        finally:
            client.close()

if __name__ == '__main__':

    que = Queue()  #线程的队列
    host = ['219.28.22.100', '219.28.22.101',
            '219.28.22.102', '219.28.22.103', '219.28.22.104']  #Ip列表
    for j in host:
        for i in range(1, 101):
            que.put((j, i))  # 1-100 是端口号  connect(ip,port) 500个元组，0ip 1端口号

    for i in range(20):
        thread1 = threading.Thread(target=test_path)
        thread1.start()
        thread1.join()
