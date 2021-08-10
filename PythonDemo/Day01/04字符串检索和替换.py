str1="this is Python project!"
#子串个数统计
val1=str1.count('is')
print(val1)

#检索子串是否存在
#如果子串存在，返回子串从左到右第一次出现的位置，如果不存在返回-1
v2=str1.find('is')
print(v2)
#如果子串存在，返回子串从左到右第一次出现的位置，如果不存在 会直接报错
#所以不推荐使用这个方法
#v3=str1.index('isx')
#print(v3)

#字符串替换的性能问题
#替换完毕，立即结束对字符串的扫描，以优化性能
newstr=str1.replace('is','**',str1.count('is'))
print(newstr)

newstr=str1.replace('is','**',str1.count('is')-1)
print(newstr)