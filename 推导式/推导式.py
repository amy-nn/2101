# 1)使用列表推导式创建一个与[1,2,3,4,5]相同的列表。
list1 = [i for i in range(1,6)]  #i for i i in ...
print(list1)

# {k:v for k in ... for v in ...}
# 2)使用列表推导从 1200 到 2000 范围内的元素创建一个列表，步长为 130。
list2 = [i for i in range(1200,2001,130)]  #步长
print(list2)
# 3)使用列表推导式构建一个新列表，计算原列表每个项目的立方
l3 = [1,2,3]
list3 = [i**3 for i in l3]
print(list3)

# 4)使用列表推导式，如果列表中元素的平方大于 50，则把列表中这个元素的平方构造一个列表。
list4 = [i for i in [2,18,46,59] if i**2 > 50]
print(list4)
# 5)生成一个新字典要求过滤掉字典中值小于5的键值对
d1= {'a':1,'b':10,'c':5}  #要大小等于5
dict5 = {k:v for k,v in d1.items() if v>=5}
print(dict5)
# 6)给定字典由车辆及其重量（以千克为单位）组成。用字典推导式返回重量在5000公斤以下的车辆名称清单。例：
dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
dict6 = {k:v for k,v in dict.items() if v<5000}
print(dict6)
# 7)创建一个新字典从score中找出语文考满分的同学  例:
d7 = {'Tom': {'chinese': 100, 'math': 100, 'english': 89},'wjx': {'chinese': 90, 'math': 100, 'english': 89}}
dict7 = {k:v for k,v in d7.items() if v['chinese'] == 100}
print(dict7)

# 8)生成一个新字典将d1中的键值对互换 例 {40:'apple', 34:'banana' , 21:'pear' }
d8 =  {40:'apple', 34:'banana' , 21:'pear' }
dict8 = {k:v for v,k in d8.items()}
print(dict8)
# 9)使用集合推倒式根据6小题的字典key生成一个新集合
set9 = {i for i in dict.keys()}
print(set9)
# 10)生成一个集合将6小题字典的value中每一项的前两个数字返回  123--12
set10 = {str(i)[0:2] for i in dict.values()}
print(set10)
# 11)用生成器推导式生成一个从10到200的生成器
tup1 = (i for i in range(10,201))
print(list(tup1))