str1="This is Python project"
# # s--> *  a--->-
tab = {115: 42, 97: 45, 106: 33}#掩码字典
newstr=str1.translate(tab) #基于字典进行字符串替换
print(newstr)  #输出替换结果

#让Python自动生成掩码字典
codeTable=str.maketrans('saj','*-!')
print(codeTable)

newstr2=str1.translate(str.maketrans('saj','*-!'))
print(newstr2)