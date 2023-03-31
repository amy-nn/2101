
def required_ints(fn):
    def inner(*args,**kwargs):
        try:
            for i in args:
                if type(i) != int:
                    raise TypeError('参数必须为整形')
            for i in kwargs.values():
                if type(i) != int:
                    raise TypeError('参数必须为整形')
        except BaseException as e:
            print(e)
        else:  #都是整数
            fn(*args,**kwargs)  #myadd()求和
    return inner

@required_ints
def my_add(*args,**kwargs):
    sum1 = 0
    for i in args:
        sum1 += i

    for i in kwargs.values():
        sum1 += i
    print(sum1)

if __name__ == '__main__':
    my_add(1, 2, 3, 65, 67, '9', a=1, b=9)

