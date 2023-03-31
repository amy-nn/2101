import multiprocessing
import os


def get_sum1():
    sum1 = 0
    for i in range(1,11):
        sum1 += i
    print(f'和是{sum1}，父进程id:{os.getppid()}，子进程id:{os.getpid()}')


def get_sum2():
    sum1 = 0
    for i in range(11,21):
        if i %2 == 0:
            sum1 += i
    print(f'和是{sum1}，父进程id:{os.getppid()}，子进程id:{os.getpid()}')

def get_sum3():
    sum1 = 0
    for i in range(20,31):
        sum1 += i
    print(f'和是{sum1}，父进程id:{os.getppid()}，子进程id:{os.getpid()}')
    with open('和.txt','w') as f:
        f.write(f'{sum1}')

if __name__ == '__main__':
    # get_sum1()
    # get_sum2()
    # get_sum3()  #主进程调
    pro1 = multiprocessing.Process(target=get_sum1)
    pro1.start()
    pro2 = multiprocessing.Process(target=get_sum2)
    pro2.start()
    pro3 = multiprocessing.Process(target=get_sum3)
    pro3.start()
