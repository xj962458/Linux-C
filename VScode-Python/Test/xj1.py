import os
def findfiles():
    path = "Day1-homework"
    filename = "2020"
    for files in os.listdir(path):
        fp = os.path.join(path, files)
        if os.path.isfile(fp) and filename in files:
            print(fp)
        elif os.path.isdir(fp):
            findfiles()

if __name__ == '__main__':
    findfiles()