#导入OS模块
import os
#待搜索的目录路径
path = "Day1-homework"
#待搜索的名称
filename = "2020"
#定义保存结果的数组
result = []

def findfiles():
    #在这里写下您的查找文件代码吧！
    i = 0
    for root, dirs, files in os.walk(path):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        
        for f in files:
            
            if filename in f:
                i=i+1
                ff=os.path.join(root, f)
                print('%d, %s'%(i, ff))
                result.append(ff)
        for j in range(len(result)):
            print(result[j])
if __name__ == '__main__':
    findfiles()
