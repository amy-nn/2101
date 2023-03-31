#装饰器  (没有参数的装饰器--默认装饰器的写法）
def outer(fn):
    def inner(*args,**kwargs):
        fn(*args,**kwargs)
    return inner

def outer2(num):  #装饰器名字
    def outer(fn):

        def inner(*args, **kwargs):
            if num > 100:
                print('参数大于100')
            else:
                print('参数小于等于100')
                fn(*args, **kwargs)  #调用被装饰的函数
        return inner
    return outer

@outer2(num=20)
def show():
    print('show')

if __name__ == '__main__':
    show()