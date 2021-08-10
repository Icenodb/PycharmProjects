l1=["1","2","3","4","5","6","100"]
#计算l1的元素累加和
#基于元素推导,快速将元素类型转换
l2=[int(e) for e in l1]
sum_l2=sum(l2)
max_l2=max(l2)
min_l2=min(l2)
len_l2=len(l2)
avg_l2=sum_l2/len_l2
print(sum_l2,max_l2,min_l2,len_l2,avg_l2)