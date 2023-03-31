import random

def loggin(fn):
    def inner(*args,**kwargs):
        #判断函数名字是不是以。。开头
        if fn.__name__.startwith('admin_'):
            print('此函数只允许被管理员调用')
            # 判断函数的参数数量
        elif len(args)+len(kwargs) > 6:
            print('参数过长')
        else:
            fn(*args,**kwargs)  #admin_calc()  calc()
    return inner


@loggin
def admin_calc():
    print('bib ovt  ---admin_calc')  #不走

@loggin
def calc():
    for i in range(100):
        num = random.randint(1,10)
        print(num)
if __name__ == '__main__':
    admin_calc()
    calc()