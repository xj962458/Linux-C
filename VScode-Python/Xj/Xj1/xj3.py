'''
*类与对象的定义
*类与对象的使用
*构造函数
*类对象和实例对象
'''
class Student():
    name = '武新纪'
    age = 0

    def PrintFile(self):
        print('name:'+self.name)
        print('age:'+str(self.age))

class Person:
    name='wuxinji'
    age=100
    salary=999999

    #构造函数
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def GetInfo(self):
        print("请输入姓名:",end='')
        self.name=input()
        print("请输入年龄:",end=' ')
        self.age=int(input())
        print("请输入薪水:",end='')
        self.salary=float(input())

    def Info(self):
        print('name:'+self.name,end=' ')
        print("age:"+str(self.age),end=' ')
        print("salary:"+str(self.salary),end=' ')
        print("打印完成")


# 实例化一个类
xj=Person('武新纪',20,999)
print('考生信息如下:')
xj.Info()
print()
print(xj.__dict__)
