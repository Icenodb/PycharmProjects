list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x, *y, z = list1
print(x, y, z)

while 1:
    info = input("enter user info:uname,phone,address?")
    if not info: break
    print(info)
