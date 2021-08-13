"""

"""

val = []
while True:
    num = input("请输入数值:")
    if not num: break
    val.append(int(num))
int_val = [e for e in val if e % 2 == 0 and e % 3 == 0]
print(int_val)
print(sum(int_val))
