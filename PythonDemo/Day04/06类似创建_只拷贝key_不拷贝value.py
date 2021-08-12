emp = {'eno': '1001', 'ename': '王兴刚', 'sex': '男', 'nation': '满族'}
# empKeyDict = emp.fromkeys(['eno', 'ename', 'nation', 'hobby'])
# print(empKeyDict)

# print(list(emp.keys()))  # 得到字典的所有的key

empKeyDict = emp.fromkeys(emp.keys())
print(empKeyDict)

print(f"hobby is {emp.get('hobby')}") #当kv不存在时 不会报错
# print(f"hobby is {emp['hobby']}") #当kv不存在时 会报错
