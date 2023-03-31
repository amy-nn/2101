import socket
import threading


#只能测一个
def test(i):
    lock.acquire() #上锁
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((i, 443))
    except BaseException as e:
        print(f'{i}地址连不上')
    else:
        print(f'{i}连接成功')
    finally:
        client.close()
    lock.release()  #解锁


if __name__ == '__main__':

    path = ['www.baidu.com','www.sina.com','www.4399.com','www.bawei.com']

    lock = threading.Lock()  #创建锁对象

    for i in path:

        # # test(i)  #执行4次
        thread1 = threading.Thread(target=test,args=(i,))
        thread1.start()

