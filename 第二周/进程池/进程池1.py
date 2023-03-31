import multiprocessing
import os
import random
import time


# 5.创建一个进程池，包含5个进程
# (1)定义一个长度为50的元组，每个元组元素内容自定义，可以为字符串也可以为数字
# (2)对元组进行遍历，分配任务给进程处理，元组元素作为进程输入处理参数
# (3)进程池中的进程打印接收到的参数信息并打印
# (4)进程池的进程每隔3秒打印xx all guys I do not like
# (5)结束所有进程，关闭进程池，主程序等待所有进程结束后，退出

def get_num(i):
    print(f'{os.getpid()}---{i} all guys I do not like')
    time.sleep(3)

if __name__ == '__main__':
    pool = multiprocessing.Pool(5)  #创建一个进程池，里面有5个进程
    tup1 = tuple(random.randint(1,100) for i in range(50))  #50个数字的元组

    for i in tup1:  #i就是每个数字
        # print(i)
        pool.apply_async(get_num,args=(i,))  #进程、线程、进程池执行函数
        # pro1 = multiprocessing.Process(target=get_num,)
    pool.close()  #只关一次，循环外
    pool.join()


