# 1)求100以内所有除以3余数 为1,2,3,5,8,9 的数   （2分）
list1 = [i for i in range(100) if i%3 in [1,2,3,5,8,9]]
# 2)求100以内所有能被3整除的数的立方（2分）
# 3)取出列表list1=['aaa','test','monging',’like’]中长度大于3的数据（2分）
# 4)List2= ['i','want','to','sleep','goodbey']  去除列表中包含 ‘e’ 且长度大于3的数据（2分）
List2= ['i','want','to','sleep','goodbey']
list4 = [i for i in List2 if i.count('e') == 0 or len(i)<=3]
print(list4)

# 5)计算出1-10之间，11-20之间的数据组成的元祖列表（2分）
list5 = [(x,y) for x in range(1,11) for y in range(11,21)]
print(list5)
# 6)List3 = [[‘test’, ‘sleep’, ‘good’], [‘computer’,‘os’,‘threading’], [‘process’,‘queue’]]
# 取出列表中长度大于3且包含 ‘e’的元素（2分）
List3 = [['test', 'sleep', 'good'], ['computer','os','threading'], ['process','queue']]
list6 = [j for i in List3 for j in i if len(j)>3 and j.count('e')]
print(list6)
# 7)List4=['T', 'D', 'K',],list5=['t', 'd', 'K',]把2个列表的元素相+组成一个新的列表（2分）
List4=['T', 'D', 'K',]
list5=['t', 'd', 'K',]
list7 = [List4[i]+list5[i] for i in range(3)]
print(list7)
# 8)Dict1 = {'name':‘david’,'age': 34, 'money': 7, 'score': 30} 把字典的key,value互换（2分）
# 9)Set1 = ['test’','computer','hight','hand','queue',threading] 用集合推导式统计字符串的长度 （2分）
# list9 = {len(i) for i in Set1}
# 10)List5= [[‘testpip’, ‘sleep’, ‘good’], [‘computer’,‘os’,‘threading’], [‘processp’,‘queue’]]，取出列表中长度大于5且包含2个以上 p的元素 包含2个（2分）

# 11)List7= ["{‘name’:’david’,‘age’:20}", “[20,30,40,50]”]将列表中的数据转换成正常格式（2分）
List7= ["{'name':'david','age':20}", "[20,30,40,50]"]
list11 = [eval(i) for i in List7]
print(list11)

# 12)List8=['陈百彤','王老大','孙晓红',‘王彤彤’]取出列表中包含彤的元素（3分）