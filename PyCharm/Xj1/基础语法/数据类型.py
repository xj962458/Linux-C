# 列表(list)
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, "what", True]
print(a)
b = [a, 3, 5, 65, 'df']
print(b)
for i in range(10):
    print(a[i]*i)
print(b[4])
print(a[0:10:2])
print(a[0:10:1])
"""
'''
# 元组(tuple)
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a)
for i in range(9):
    print(a[i])
print(type(a))
'''
'''
# 集合(set)
a = {1, 2, 3, 45, 65, 1, 2, 34}
b = {1, 2, 3}
print(a)
print(3 in a)
print(b)
print(a - b)
print(a | b)
print(a & b)
'''

# 字典
a = {
    1: "C语言",
    2: "C++",
    3: "Java",
    4: "Python",
    5: 6666,
    }

print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
