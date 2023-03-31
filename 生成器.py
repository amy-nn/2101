#函数里面有yield

def show1():
    a = 1
    b = 1 #前两个数字都是1  1  2 3  5...
    for i in range(50):
        yield a  #return
        a,b = b,a+b

num = show1()
print(list(num)[-1])

n = [1,2,1,2,1,2,1,2,3,4,5,3,-3,-10,-6]
# n=[1,2,3,4,5,-3,-10,-6]

def show2():
    n1= []  #去重
    for i in n:
        if i not in n1:  #不在放到新列表
            n1.append(i)
            yield i  #返回

list2 = show2()
print(list(list2))

lst = [10,20,1,2,41,22,1,2,3,4,5,3,-3,-10,-6]
#（0，1）（1，2）.。。（9，10）（0，1）。。。（19，20）
def show3():
    for i in lst:  #10
        for j in range(0,i): # 0 1 2 3 4 5 6 7 8
            yield (j,j+1)
list3 = show3()
print(list(list3))



