name=["罗斯福","林肯","奥巴马","川建国","拜登"]
sc=(30,20,80,90)
state="00111"
# for n in name:
#     eindex=name.index(n)
#     print(f"{n}总统,{sc[eindex]}分")
"""
1.并行迭代的序列，元素数据类型可以不同，并且序列的类型也可以不同
2.并行迭代，按最短匹配迭代
3.并行迭代，可以同时迭代N多个序列
"""
for n,s,se in zip(name,sc,state):
    '''
           if 判断如果成立,就将'依然潜伏'  赋值给msg
           否则将  '光荣地挂了' 赋值给msg

           等价于java的 冒号表达式:
               msg=se.equals('1')?'依然潜伏':'光荣地挂了'
    '''
    msg="依然潜伏" if int(se) else "光荣地挂了"
    print(f"总统{n},在获得{s}分以后,{msg}")