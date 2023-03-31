import multiprocessing
import os

def check_num(start,end,que):
    for num in range(start, end+1):
        for i in range(2,num):  #把1和本身去了
            if num %i == 0:  #不是一个质数了
                break
        else:
            print(f'父进程：{os.getppid()}--子进程：{os.getpid()},{num}')  #是一个质数
            que.put(num)
            with open('a.txt','a') as f:
                f.write(f'{num}\n')
                

if __name__ == '__main__':
    list1 = [0,1000,2000]
    que = multiprocessing.Queue()
    list2 = []

    for i in range(3): #0 1 2
        pro1 = multiprocessing.Process(target=check_num,args=(list1[i],list1[i]+1000,que))
        pro1.start()
        pro1.join()


    # while not que.empty():
    #     list2.append(que.get())
    # print(list2)

    while True:
        if que.empty():
            break
        else:
            list2.append(que.get())
    print(list2)



