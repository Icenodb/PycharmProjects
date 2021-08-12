from copy import deepcopy

stu1 = {'name': '王重阳', 'course': ['Java', 'Python', 'Julia']}
# 克隆stu1
stu2 = deepcopy(stu1)
stu2['name'] = '赵奇兵'
stu2['course'][:] = ['喝酒', '吃肉', '逛街']

# 对象分析
print(stu1)
print(f"stu1={hex(id(stu1))},sut1.name={hex(id(stu1['name']))}", end='')
print(f",stu1.course={hex(id(stu1['course']))}")
print(stu2)
print(f"stu2={hex(id(stu2))},sut2.name={hex(id(stu2['name']))}", end='')
print(f",stu2.course={hex(id(stu2['course']))}")
