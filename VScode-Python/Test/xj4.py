# 函数
print()
a = 3.1415926
b=100
print(round(a,4))

def Printf():
    print("这里是考生管理系统")
    print("1、输入考生信息")
    print("2、输出考生信息")
    print("3、插入考生信息")
    print("4、删除考生信息")
    print("5、保存考生信息")

def fun(a=1,b=2):
    return a+b,a*b,a-b

# f1,f2,f3=fun(a,b)
#f1,f2,f3=fun()
#f1,f2,f3=fun(1,)
f1,f2,f3=fun(9)

print(f1,f2,f3)
print(type(fun(a,b)))
print(fun(a,b))
x=Printf()
print(x)

