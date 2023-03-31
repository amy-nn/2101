import multiprocessing
import os




def get_sum():
    sum = 0
    for i in  range(1,101):
        sum+= i
    print(f'和是{sum},父编号：{os.getppid()},子进程：{os.getpid()}')

def show():
    print('show')

if __name__ == '__main__':
    #进程间不共享数据（数据间通信造队列来完成）
    pro1 = multiprocessing.Process(target=get_sum)
    pro1.start()

    pro2 = multiprocessing.Process(target=show)
    pro2.start()