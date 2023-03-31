# （一）创建名为d1.py的文件，实现一个装饰器名称为check_types检查函数参数  （20分)
# 例：
# @check_types(str)  确保函数接收到的每一个参数都是str类型
# 具体要求：
# 1）check_types为带参数的通用装饰器，可以装饰任何函数。包括不定长参数函数、带返回值函数等
# 2）check_types的参数取值有3种分别为 int、str、float
# 3）check_types 支持1个参数
# 4）如果参数不满足条件,打印 TypeError:参数必须为xxxx类型

def check_types(args1):
    def outer(fn):
        def inner(*args,**kwargs): #参数能用不定长
            try:
                if type(args1) !=int and type(args1) !=str and type(args1) !=float:
                    raise TypeError('参数必须为int,str,float类型')  #抛异常
            except BaseException as e:
                print(e)
            else:
                #没报错
                num = fn(*args,**kwargs)  #带返回值函数  fn=show,num=show的返回值
                print(num)  #没关系的
                return num
        return inner
    return outer

# @check_types('hello')
# @check_types(1)
@check_types(True)
# @check_types(12.0)
def show():
    print('show')


if __name__ == '__main__':
    show()


