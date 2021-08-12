emp = {'eno': '1001', 'ename': '王兴刚', 'sex': '男', 'nation': '满族'}
# #.读取所有的键值对形成列表
# itemList=emp.items()
# print(itemList)  #[('eno', '1001'), ('ename', '王兴刚'), ('sex', '男'), ('nation', '满族')]

# 基于for 遍历键值对
for key, value in emp.items():  # 序列解包
    print(f"{key}={value}")

# 序列解包
seq1 = ('王兴刚', '王重阳', '王阳明')
name1, name2, name3 = seq1
print(f"name1={name1},name2={name2},name3={name3}")
