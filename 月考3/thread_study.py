# 1)做一个要是用户名统计的程序,随机生成3000个8位数用户名包含大小写字母
# 2)把生成的用户名去重后放入队列中。  列表变集合
# 3)程序至少启动5个线程平均分配处理数据。
# 4)子线程分别统计用户名中每个字符出现的次数。
# 5)把每个线程的结果存入到txt文件中
# 6)读取txt文件,最后以字典格式输出结果[{线程1的id:[结果]},{ {线程2的id:[结果]}…..]。
import multiprocessing
import random
import string
import threading
from queue import Queue

def show():
    str_dict = {}
    str_list = []  #列表里放了600个字典
    for i in range(600):
        str1 = que.get()  #字符串
        dict1 = {k:str1.count(k) for k in str1}  #600个  {a:1...b:2}
        str_list.append(dict1)  #[{},{}...600个{}]
    str_dict[threading.currentThread().name] = str_list
    print(f'{str_dict}')
    with open('月考线程.txt','a') as f:
        f.write(f'{str_dict}\n')


if __name__ == '__main__':
    que = Queue() #线程的队列

    set1 = set()  #集合 自带去重的功能
    for i in range(3000):
        str1 = ''.join(random.choices(string.ascii_letters+string.digits,k=8))  #生成随机数
        set1.add(str1)
    # print(len(set1))  #3000
    for i in set1:  #i是每个随机数
        que.put(i)

    for i in range(5):
        thread1 = threading.Thread(target=show)
        thread1.start()
        thread1.join()

    #读取5个字典放到到列表中
    list_all= []
    with open('月考线程.txt','r') as f:
        list_all.append(f.read())
    print(list_all)
