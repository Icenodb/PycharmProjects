#奇偶分加
sum1,sum2=0,0
for i in range(1,16):
    if i%2==0:
        sum1=sum1+i
    else:
        sum2=sum2+i

print(f"偶数和={sum1:10},\n奇数和={sum2:10}")



#变量的内存管理方式
# f1,f2=0,0
# f3=0
# f4=0
# f4=f4+1
# f5=1
# print(id(f1))
# print(id(f2))
# print(id(f3))
# print(id(f4))
# print(id(f5))


#在技术可行性与代码可读性之间,选择代码可读性
# sum1,sum2=0,0
# for i in range(1,11):pass
# print(i)

# i=i+100
# print(i)
