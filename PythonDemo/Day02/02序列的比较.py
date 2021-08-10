s1=[1,2,5,8,0]
s2=s1[:]  #序列切片,相当于将s1复制一份,赋值给s2
s3=s1

b1=s1==s2  #内容比较
#id  查看对象的内存地址
print(f"b1={b1}")
b2=s1 is s2  #对象比较
print(f"b2={b2}")

b3=s1 is s3
print(f"b3={b3}")

print(f"s1_id={id(s1)},\ns2_id={id(s2)},\ns3_id={id(s3)}")
