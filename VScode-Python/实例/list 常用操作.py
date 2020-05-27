#list 定义
li = ["a", "b", "mpilgrim", "z", "example"]
li
li[1]  

#list 负数索引
li
li[-1]
li[-3]
li
li[1:3]
li[1:-1]
li[0:3]

#list 增加元素
li
li.append("new")
li
li.insert(2, "new")
li
li.extend(["two", "elements"])
li

#list搜索
li
li.index("new")
li.index*("c")
"c" in li

#list删除元素
li
li.remove("z")
li
li.remove("new")    # 删除首次出现的一个值
li.remove("c")     #list 中没有找到值, Python 会引发一个异常
li.pop()      # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
li

#list运算符
li = ['a', 'b', 'mpilgrim']
li = li + ['example', 'new']
li
li += ['two']  
li
li = [1, 2] * 3
li

#使用join链接list成为字符串
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
["%s=%s" % (k, v) for k, v in params.items()]
";".join(["%s=%s" % (k, v) for k, v in params.items()])

#list 分割字符串
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
s
s.split(";")  
s.split(";", 1)

#list 的映射解析
li = [1, 9, 8, 4]
[elem*2 for elem in li]   
li
li = [elem*2 for elem in li]
li

#dictionary 中的解析
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
params.keys()
params.values()
params.items()
[k for k, v in params.items()]
[v for k, v in params.items()]
["%s=%s" % (k, v) for k, v in params.items()]

#list 过滤
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
[elem for elem in li if len(elem) > 1]
[elem for elem in li if elem != "b"]
[elem for elem in li if li.count(elem) == 1]
