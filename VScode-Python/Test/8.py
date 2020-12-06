a = [10, 34, 23, 21, 54, 34, 23, 23]
with open("data.txt", 'w') as f:
    for i in a:
        f.write(str(i)+'\n')
with open("data.txt", 'r') as f:
    b = list(map(int, f.readlines()))
    b.sort()
with open("data_asc.txt", 'w') as f:
    for i in b:
        f.write(str(i)+'\n')
