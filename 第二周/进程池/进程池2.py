import multiprocessing
import os
import random
import time


def msg(i):
    print(f'{os.getpid()}--这是第{i}个任务')
    time.sleep(random.randint(1,3))


if __name__ == '__main__':
    pool = multiprocessing.Pool(3)

    for i in range(1,11):
        pool.apply_async(msg,args=(i,))
    pool.close()
    pool.join()