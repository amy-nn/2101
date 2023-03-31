# 请设计一个带参数的通用装饰器timeit它可作用于任何函数上，并打印该函数的执行时间并支持时间单位转换。注意代码规范，请在合适的位置添加注释
# 要求：
# 1)装饰器支持无参数也支持带一个参数
# 2)实现一个通用装饰器，它可以作用在任何函数上
# 3)装饰器参数名unit 取值ms 或 s。当值为ms时打印函数的执行时间单位为毫秒。当值为s时打印执行时间单位为秒
# 4)当不传参数时默认为ms
# 5)实现带不定长参数并有返回值的my_sub函数并用装饰器装饰。功能：计算所有传入参数的差。 例：my_sub(1,2,3,65,67,5,a=1,b=2)
# 6)调用函数并能打印出正确结果和正确的执行时间
# 装饰器示例：
# @timeit(unit=’ms’)
# @timeit(unit=’s’)
# @timeit()
import time


def timeit(unit='ms'):
    def outer(fn):
        def inner(*args,**kwargs):  #通用
            start = time.time()  #毫秒
            fn(*args,**kwargs)  #调用函数
            end = time.time()
            if unit == 'ms':
                print(f'当前函数的运行时间是{end-start}毫秒')
            else:
                print(f'当前函数的运行时间是{(end-start)/1000}秒')
        return inner
    return outer

@timeit()
def my_sub(*args,**kwargs):  #通用不定长的参数列表
    diff = args[0]  #默认给下标0
    for i in range(1,3):  #从1到长度结束
        diff -= args[i]

    for i in kwargs.values():  #遍历 字典，拿到字典中所有的值
        diff-= i
    print(diff)

if __name__ == '__main__':
    my_sub(1,2,3,a=1,b=2)
