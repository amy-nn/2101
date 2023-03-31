import multiprocessing
import random


def make_num(que):
    for i in range(5):
        num = random.randint(1,10)
        que.put(num)
        print(num)

def check_num(que,que2):
    list2 = []  #列表
    while not que.empty():
        list2.append(que.get())

    list3 = [[x,y,z] for x in list2 for y in list2 for z in list2 if x+y>z and x+z>y and z+y>x
             and x!=y and y!=z and z!=x]
    que2.put(list3)  #放了一次
    print(f'共有{len(list3)}个三角形')

def get_sum(que2):
    list3 = que2.get()  #取出一个大列表（6个小列表）
    for i in list3:
        sum = i[0]+i[1]+i[2]
        print(f'三角形{i},周长是{sum}')

if __name__ == '__main__':
    que = multiprocessing.Queue() #创建队列  进程1放--进程2取
    que2 = multiprocessing.Queue()  #进程2放--进程3取

    pro1 = multiprocessing.Process(target=make_num,args=(que,))
    pro1.start()
    pro1.join()

    pro2 = multiprocessing.Process(target=check_num,args=(que,que2))
    pro2.start()
    pro2.join()

    pro3 = multiprocessing.Process(target=get_sum, args=(que2,))
    pro3.start()
    pro3.join()





