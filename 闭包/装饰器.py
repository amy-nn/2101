#闭包--装饰器
#1.函数套函数  2.内用外变量  3.外返内函数名
#装饰器
import time


def outer(fn):  #test()
    def inner():
        start = time.time()
        fn()  #test()  1-100万的和
        end = time.time()
        print(f'花费的时间是{end-start}')
    return inner


@outer  #调用装饰器
#被装饰
def test():
    sum1 = 0
    for i in range(1,1000000):
        sum1 += i
    print(sum1)

if __name__ == '__main__':
    test()


