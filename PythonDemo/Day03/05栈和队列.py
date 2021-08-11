

urlList=['www.baidu.com','www.360doc.com','www.copenedu.com']
#基于队列的原理读取列表
# while urlList:#在python中,非空就是True
#     e=urlList.pop(0)
#     print(e)
# print(urlList)

#基于栈的原理，读取列表：
# while urlList:
#     e=urlList.pop()
#     print(e)
# print(urlList)

#遍历列表
for e in urlList:
    print(e)
print(urlList)

#在for...in...循环中，不要改变序列的构成元素
numList=[0,1,2,3,4,5,6,7,8,9]
for e in numList:
    print(e)
    numList.remove(e)
print(numList)
