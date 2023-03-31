# 4.创建threading_3.py文件，用多线程去实现多任务，主线程生成1-1000的数字。
# (1)将数字依次放入队列，并创建5个线程从队列中取数据并平均去处理
# (2)线程处理数据，取出其中是水仙花数的数据，并打印。
import threading
from queue import Queue  #线程
import multiprocessing  #进程

def get_num():
    #线程要执行的逻辑
    for i in range(200):
        num = que.get()  #num是要判断的数字
        num1 = num//100%10  #百位
        num2 = num//10%10  #十位
        num3 = num%10  #个位
        if num1**3 + num2**3 + num3**3 == num and num>100:
            print(f'{threading.currentThread().name}--{num}')

if __name__ == '__main__':
    que = Queue()
    # que = multiprocessing.Queue()
    # que = multiprocessing.Manager().Queue()

    for i in range(1,1001):
        que.put(i)

    for i in range(5):
        thread1 = threading.Thread(target=get_num)
        thread1.start()
        thread1.join()




