def callRef(data:dict):
    #对参数进行的改变
    data["name"]="啊这"
    print(f"参数的内容是:{data}")

def callByValue(x:int,y:int):
    print(f"x_id={id(x)}")
    #对参数进行改变
    x+=100
    y+=10
    z=x+y
    print(f"x={x},y={y},z={z}")
    print(f"x address={id(x)}")


if __name__ == "__main__":
    # d1 = dict(eid="1001")
    # callRef(d1)
    # print(d1)

    a=b=10
    callByValue(a,b)
    print(f"a={a},a_id={id(a)},b={b}")

