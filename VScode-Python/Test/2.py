ls = ["清华大学", "北京大学", "中国人民大学", "北京航天大学","北京师范大学"]
with open("test.txt",'w') as f:
    for i in ls:
        f.write(i+'\n')
with open("test.txt",'r') as f1,open("test副本.txt",'w') as f2:
    for line in f1.readlines():
        f2.write(line)
        print(line.strip('\n'))
    