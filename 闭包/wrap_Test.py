from functools import  wraps
def outer(fn):
    @wraps(fn)  #保护函数名字不被改变
    def inner(*args,**kwargs):
        fn(*args,**kwargs)
    return inner

def outer2():
    def outer(fn):
        @wraps(fn)  # 保护函数名字不被改变
        def inner(*args, **kwargs):
            fn(*args, **kwargs)
        return inner
    return outer

@outer
def show():
    pass

if __name__ == '__main__':
    show()
    print(show.__name__)  #show()