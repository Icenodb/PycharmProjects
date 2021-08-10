#斐波那契数列函数
def Fibonacci(endMonth:int):
    print(endMonth,type(endMonth))
    fibs = [1,1]
    for m in range(3,endMonth+1):
        fibs.append(fibs[-1]+fibs[-2])
    count=0
    for e in fibs:
        print(f"{e:>10}",end=' ')
        count+=1
        if count==6:
            print()
            count=0
#调用上面定义的函数
if __name__=='__main__':
    Fibonacci(30)

# #方案3:基于python的序列
# fibs  =  [1,1]
# #index    0 1
# #index   -2 -1
# for m in range(3,37):
#     #向序列中,追加元素
#     fibs.append(fibs[-1]+fibs[-2])

# #格式化输出
# count=0  #每行元素的个数
# for e in fibs:
#     print(f"{e:>10}",end=' ')
#     count+=1
#     if count==6:  #每行6个元素
#         print()   #空的print表示换行
#         count=0   #计数器清零




# #方案2,每次算两个值---跟踪每个变量在每个时间点运行状态
# f1=f2=1
# for m in range(3,37,2):  #m=5
#     f1=f1+f2  #2,5
#     f2=f2+f1  #3,8
#     print(f"第{m}个月兔子的数量是{f1}")
#     print(f"第{m+1}个月兔子的数量是{f2}")


#方案1,每次算一个
# f1=f2=1
# for m in range(3,37):
#     fsum=f1+f2
#     print(f"第{m}个月兔子的数量是{fsum}")
#     f1=f2
#     f2=fsum