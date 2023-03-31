import multiprocessing


def show(que,start,end):
    list2 = []
    for i in range(start,end):
        if i %2  == 0 and i%3 == 0:
            list2.append(i)
    que.put(list2)
    with open('a.txt','a') as f:
        f.write(f'{list2}\n')


if __name__ == '__main__':

    que = multiprocessing.Queue()  #队列
    list1 = [1,250,500,750]

    list3 = []

    for i in range(4):  #i= 0(1) 1(250) 2 3
        pro1 = multiprocessing.Process(target=show,args=(que,list1[i],list1[i]+250))
        pro1.start()
        pro1.join()

    with open('a.txt','r') as f:
        list3.append(f.read())
    print(list3)




