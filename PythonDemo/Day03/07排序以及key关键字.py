#sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

#语法sorted(iterable, key=None, reverse=False)

methodList=["Add","Query","findById","Modify","BathDelete","deleteById"]
# methodList.sort(key=len)
methodList.sort(key=str.lower,reverse=True)
print(methodList)