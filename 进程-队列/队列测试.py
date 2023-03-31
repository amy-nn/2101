# 1）开启四个进程
# 2）2个进程做为生产者 往队列中写入10000个随机数
# 3）另外2个进程从队列中读取并输出随机数。 同时打印父进程id，主进程id和随机数。输出后进程执行sleep(0.5)
import multiprocessing
import os
import random


def put_num(que):
    for i in range(100):
        que.put(random.randint(1,200))

def get_num(que):
    for i in range(100):
        print(f'{os.getppid()}--{os.getpid()}----{que.get()}')

if __name__ == '__main__':
    que = multiprocessing.Queue() #创建队列

    for i in range(2):
        pro1 = multiprocessing.Process(target=put_num,args=(que,))
        pro1.start()
        pro1.join()
    # print(que.qsize())

    pro3 = multiprocessing.Process(target=get_num, args=(que,))
    pro3.start()
    pro3.join()  #取完了

    pro2 = multiprocessing.Process(target=get_num, args=(que,))
    pro2.start()
    pro2.join()



