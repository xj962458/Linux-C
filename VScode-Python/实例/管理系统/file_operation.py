# @Author  : Fizzyi
import json

def basic_file_read(file):
    #普通文本文件的读取
    with open(file,'r',encoding='utf-8') as f:
        return f.read()

def basic_file_write(file,content):
    #普通文本文件的写
    content = json.dumps(content)
    with open(file,'w',encoding='utf-8') as f:
        f.write(content)