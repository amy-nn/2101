num = 10  #全局变量
def outer():
    a = 20
    def inner():
        global num   #global
        nonlocal a
        num = 100
        a = 200
        print(num)
    return inner

print(num)

#当内部函数要修改全局变量的时候加global
#当内部函数要修改外部变量的时候加nonlocal
