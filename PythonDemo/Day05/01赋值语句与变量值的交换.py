a, b, c = 3, 5, 0
print(f"a={a},b={b},c={c}")
# 交换两个变量的值
c = b
b = a
a = c
print(f"a={a},b={b},c={c}")

# python中还可以这样做
a, b = b, a
print(f"a={a},b={b},c={c}")
