import multiprocessing
import os
import threading


def show1():
    print('第一任务  宋斌考试')
def show2():
    print(int('第一任务  乔智豪考试'))  #出错
def show3():
    print('第一任务  张博考试')  #出错
    print(f'父进程的编号{os.getppid()}，子进程编号{os.getpid()}')


def show4(num):
    print(f'父进程的编号{os.getppid()}，子进程编号{os.getpid()}')

if __name__ == '__main__':
    # show1()  #主进程
    # show2()
    # show3()
    # pro1 = multiprocessing.Process(target=函数名,args=(10,))
    pro1 = multiprocessing.Process(target=show4,args=(10,))  #子进程
    pro1.start()

    pro2 = multiprocessing.Process(target=show3)
    pro2.start()
