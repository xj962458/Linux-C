# 人民币与美元相互兑换
money=input("请输入带有符号的货币:")
if money[-1] in ['￥']:
    m=(eval(money[0:-1])/6)
    print("可兑换美元{:.2f}$".format(m))
elif money[-1] in ['$']:
    m=6*eval(money[0:-1])
    print("可兑换人民币{:.2f}￥".format(m))
else:
    print("输入错误")
