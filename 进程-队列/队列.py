import multiprocessing
import os
import random
def make_num(queue):
    for i in range(10):
        num = random.randint(1,100)
        print(f'{os.getpid()}--{num}')
        queue.put(num) #把随机数放到队列中
    # print(queue.qsize())

def get_num(que):
    #从队列中把数字全部取出来
    while not que.empty():
        num = que.get()
        print(f'{os.getpid()}--{num}')

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    pro1 = multiprocessing.Process(target=make_num,args=(queue,))
    pro1.start()  #放
    pro1.join()  #保证进程的执行顺序
    pro2 = multiprocessing.Process(target=get_num,args=(queue,))
    pro2.start()  #取
    pro2.join()



