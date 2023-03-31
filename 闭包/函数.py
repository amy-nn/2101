# def 函数名(参数):
#     print('函数体')


# def show():  #无参无返的函数
#     print('show')
#
# show()

# def hello(name):  #变量
#     print(f'{name}你好')
# hello('王嘉轩')

# def hello(name):
#     name()  #函数（函数作为参数）
#
# def name():
#     print('这是name函数')
# hello(name)

# def show():
#     return 10
#
# num = show()
# print(num)  #10

def show1():
    def name():
        print('内部函数')
    return name
name = show1()
name()  #调用函数

#函数可以作为参数   函数可以作为返回值
