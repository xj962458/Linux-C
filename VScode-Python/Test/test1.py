#导入OS模块
import os

#定义保存结果的数组
result = []
def search():
    i=0
    #待搜索的目录路径
    path = "C:/Users/xjfyt/Desktop/Python/VScode-Python"
    #待搜索的名称
    word = "xj"
    for files in os.listdir(path):
        fp = os.path.join(path, files)
        if os.path.isfile(fp) and word in files:
            result.append(fp)
            print(fp)
            i=i+1
        elif os.path.isdir(fp):
            search()

search()