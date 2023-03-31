import multiprocessing

def get_num1(que,n1,n2):
    #153 = 1**3+5**3+3**3
    for i in range(n1,n2):
        n1 = i%10
        n2 = i//10%10
        n3 = i//100%10  #取整
        if n1**3+n2**3+n3**3 == i:
            #放
            que.put(i)

if __name__ == '__main__':
    list1 = []
    list2 = [1,1001,2001]
    que = multiprocessing.Queue()
    for i in range(3):
        pro1 = multiprocessing.Process(target=get_num1,args=(que,list2[i],list2[i]+1000))
        pro1.start()
        pro1.join()

    #从队列中取
    while not que.empty():  #一直取
        list1.append(que.get())
    print(list1)