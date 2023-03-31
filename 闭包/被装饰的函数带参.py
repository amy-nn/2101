import time


def outer(fn):
    def inner():
        fn()
    return inner  #被装饰的函数无参

def outer2(fn):
    def inner(*args,**kwargs):
        start = time.time()
        sum1 = fn(*args,**kwargs)  #函数的调用  my_sum()
        print(sum1)
        end = time.time()
        print(f'{end - start}')  #结束时间减去开始时间 = 花费时间
        
        #把fn是被装饰的函数名写入到文件
        with open('log.txt','a') as f:
            f.write(f'{fn.__name__}')  #fn.__name__得到函数的名字
    return inner  #有参或无参的函数

@outer2
def my_sum():
    sum1 = 0
    for i in range(1,100000):
        sum1+=i
    return sum1

if __name__ == '__main__':
    my_sum()