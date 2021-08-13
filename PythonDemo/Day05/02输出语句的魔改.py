'''
1.同时输出多项数据
'''
# ename='王兴刚'
# idcard='8798989890809809'
# yhkh='6666 7777 8888 9999'
# money='12345678.9'
# print(ename,idcard,yhkh,money,sep='#')
# print("this is sal info")

'''
2.print的结束符合,可以被改变
  print默认情况下,以\n为输出结束符,
  可以通过修改end参数的值,改变结束符
'''
for e in range(1,10):
    print(e,end=',')
print(10)

