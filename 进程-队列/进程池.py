#进程池用来管理进程
import multiprocessing
import os
import random


def put_num(que):
    for i in range(5000000):
        que.put(random.randint(1,20000))
def get_num(que):
    for i in range(5000000):
        print(f'父进程id:{os.getppid()}---子进程id:{os.getpid()}---{que.get()}')

if __name__ == '__main__':

    #1.创建进程池
    pool = multiprocessing.Pool(4) #池子中有4个进程
    # que = multiprocessing.Queue()#进程队列
    # que = Queue() #线程队列
    que = multiprocessing.Manager().Queue()  #进程池的队列

     #2.添加进程池的函数
    for i in range(2):
        #放  apply_async(函数)
        pool.apply_async(put_num,args=(que,))
    for i in range(2):
        #取  apply_async（函数）
        pool.apply_async(get_num, args=(que,))
    # 3.关闭进程池
    pool.close()
    pool.join()