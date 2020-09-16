# 温度转换
item=input("请输入您选择的转换方式:\n1、华氏转摄氏\n2、摄氏转华氏\n")
if item=='1':
    tempStr=(eval(input("请输入您要转换的华氏温度:"))-32)/1.8
    print("转换后的摄氏温度是{:.0f}C".format(tempStr))
elif item=='2':
    tempStr=(eval(input("请输入您要转换的摄氏温度:"))*1.8)+32
    print("转换后的华氏温度是{:.0f}F".format(tempStr))
else:
    print("输入错误！")

