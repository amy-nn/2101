#1.函数套函数  2.内部函数用外部函数的变量   3.外部函数返回内部函数的名字

def outer():  #外部函数
    num = 20
    print(num)
    def show(): #内部函数
        print(num) #打印外部函数的变量
    return show

# show = outer() #show函数
# show()
show = outer()
show()
