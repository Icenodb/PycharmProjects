# 字典是另一种可变容器模型，且可存储任意类型对象。
# 创建字典
dicts = {"name": "李白", "age": "30"}
print(dicts)
print("dicts[name]:",dicts["name"])
print("dicts[age]:",dicts["age"])

# print("dicts[alice]",dicts["Alice"])
# 如果用字典没有的键访问数据,会报错如下
# Traceback (most recent call last):
#   File "C:\Users\xxx\Projects\PythonDemo\Day03\08列表元组字典集合.py", line 8, in <module>
#     print("dicts[alice]",dicts["Alice"])
# KeyError: 'Alice'

#修改字典
dicts["age"]=25 #更新age
dicts["job"]="诗人"  #添加信息
print(dicts)

#删除字典元素
#能删除单一元素也能清空字典
del dicts["job"] #删除键
print(dicts,type(dicts))
dicts.clear()  #清空字典
print(dicts)
del dicts  #删除字典
# print(dicts)

#字典键特性:
#1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
#2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行