
def callByValue(x:int,y:int):
    """
    不可变对象参数
    :param x:
    :param y:
    """
    z=x+y
    print(f"x={x},y={y},z={z}")

if __name__=="__main__":
    #顺序传参---参数按定义顺序，依次接收数据
    callByValue(100,20)
    #按名传参---此时可以忽略函数定义时候的参数顺序
    callByValue(x=20,y=100)
    callByValue(y=100,x=20)