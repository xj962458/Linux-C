def Trans(f):
    return (f-32)*5/9
def main():
    f = eval(input("请输入一个华氏温度:\n"))
    print("{:.2f}℉转换为摄氏温度是{:.2f}℃".format(f, Trans(f)))
main()
