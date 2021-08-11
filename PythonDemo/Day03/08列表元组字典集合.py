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