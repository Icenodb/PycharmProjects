#定义空的字典
# d1={}
# d2=dict()
# print(type(d1),type(d2))

#基于具体数据,创建字典
# emp={"eid":"1002","ename":"汪伦","sex":"男","nation":"汉族"}
# print(emp)

#基于参数名与参数值创建字典
# emp=dict(eid="E1005",ename="李白",sex="男",
#          nation="汉族",hobby="1，2，3")
# print(emp)

#转换序列构成字典--可以是列表嵌套列表,但是建议列表嵌套元组
people=[("eid","E2005"),("ename","杜甫"),("sex","男")]
emp=dict(people)
print(emp)