
#创建空的list
#实际上是在调用list类的构造子
list1=list()
print(list1)

list2=[]
print(list2)

#为构造子提供参数
l2=list(range(1,10))#以指定的序列充当list类的构造子，构造新的列表
print(l2)

tuple1=(1,2,3,4,5)
l3=list(tuple1) #接收元组参数
print(l3)

ltem=[5,6,7,8]
l4=list(ltem) #接收列表参数
print((f"l4={l4}",ltem is l4))

l5=list("hello world")#接收字符串参数
print(l5)