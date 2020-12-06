i = 0
a=[]
with open("test2.txt",'r') as f:
    print("文件内容如下:")
    for line in f.readlines():
        a.append(len(line))
        print(line.strip('\n'))
        i+=1
dict1=dict(zip([j+1 for j in range(i)],a))
items = list(dict1.items())
items.sort(key=lambda x: x[1], reverse=True)
print("该文件有{}行".format(i))
print("包含字符数目最多的是{}行".format(items[0][0]))
print("包含字符数目最少的是{}行".format(items[-1][0]))
