import threading


def find_apple(str1):
    count1 = str1.count('apple')
    print(f'{threading.currentThread().name}----从{str1}这个字符串中，找到{count1}个apple')
    with open(f'{threading.currentThread().name}.txt','w') as f:
        f.write(f'{count1}')


if __name__ == '__main__':
    # 1.读全部的文件内容
    with open('test3.txt', 'r') as f:
        str1 = f.read()
    print(str1)
    # 3.把读出来的内容分两部分，用slipt('。'）
    strlist = str1.split('。') #列表

    for str1 in strlist:  # 执行2次
        thread1 = threading.Thread(target=find_apple, args=(str1,))
        thread1.start()
        thread1.join()

    #5.读两个文件，求和
    sum = 0
    files = ['Thread-1.txt','Thread-2.txt']
    for i in files:
        with open(i,'r') as f:
            sum+= int(f.read())

    print(f'统计结束 全文共出现关键字{sum}次')

