l1=[1,2,3,4,5,6,7,8,9]
last=l1[-3:]#基于负索引的切片---获取后三个元素
print(last)

s2=l1[::2]
print(s2)
s1=l1[80:100:3]#进行切片的时候下标越界 不会报错
print(s1)
subL1=l1[1:6] #截取区间元素
print(subL1)
subL2=l1[3:]#从下标3截取到最后
print(subL2)
subL3=l1[:6]#从开始到6为止 不包含6
print(subL3)