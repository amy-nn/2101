#from来自于decorator这个文件 引用  两个装饰器
from  decorator import cost_time,logging

@cost_time
@logging
def show():
    try:
        a = 0
        b = 20
        c = a+b
    except BaseException as e:
        return e
    else:
        return c
if __name__ == '__main__':
    show()


