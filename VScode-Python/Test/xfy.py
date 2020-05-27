import os
def search(path, word):
    i=0
    for files in os.listdir(path):
        fp = os.path.join(path, files)
        if os.path.isfile(fp) and word in files:
            result[i]=fp
            print(fp)
            i=i+1
        elif os.path.isdir(fp):
            search(fp, word)

search("C:/Users/xjfyt/Desktop/Python/VScode-Python", "xj")