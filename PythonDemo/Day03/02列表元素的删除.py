#按元素删除---先判断后再删除
l1=[1,2,3,4,5,6,7,8]
if 20 in l1:
    l1.remove(20)
print(l1)

#将所有的2都删除
while 2 in l1:
    l1.remove(2)
print(l1)

#基于索引删除的语法 del指令
l2=[1,2,3,4,5,6,7,8]
del l2[3]#下标如果越界 会报错
print(l2)