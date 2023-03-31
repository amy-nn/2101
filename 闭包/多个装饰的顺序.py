def outer(fn):
    print('这是第一个装饰器')
    def inner(*args,**kwargs):
        fn(*args,**kwargs)
    return inner

def outer2(fn):
    print('这是第二个装饰器')
    def inner(*args,**kwargs):
        fn(*args,**kwargs)
    return inner

@outer  #语法糖 （甜）
@outer2  #离的近先执行
def show():
    print('show')