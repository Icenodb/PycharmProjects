# l1=[1,2,3,4,5,6,7,8,9]
# #转置的两种方式
# #1.临时转置 将转置后的元素放入一个新的列表 原列表不变
# #基于内置函数 reversed() 实现
# rl1=reversed(l1)
# print(l1)
# print(list(rl1))
#
# #2.永久转置 基于list的reverse() 方法
# l1.reverse()
# print(l1)

# t1=(1,2,3,4,5,6)
# tem_list=list(t1)
# tem_list.reverse()
# print(tem_list)
#
# newT1=tuple(tem_list)
# print(newT1)