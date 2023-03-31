import multiprocessing


def replace_str(i,dict1,que):
    #1.反转
    str2 = i[::-1]  #my  --ym
    # print(str2)

    #2.替换
    for k,v in dict1.items():
        if k in str2:
            str2 = str2.replace(k,str(v))
    # 3.加前缀
    str3 = 'sec'+str2
    que.put(str3)  #把结果放到队列中

if __name__ == '__main__':
    dict1 = {'a':9,'b':8,'c':7,'d':6,'e':5}
    str1 = 'my name is cake'
    list1 = str1.split(' ')
    que = multiprocessing.Queue()

    for i in list1:
        # print(i)  #i是每一个字符串
        pro1 = multiprocessing.Process(target=replace_str,args=(i,dict1,que))
        pro1.start()
        pro1.join()

    #循环得到队列中的内容
    while not que.empty():
        str4 = que.get()
        print(str4)