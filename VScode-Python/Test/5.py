import numpy as np

a = np.random.randint(100, 201, 20).reshape(4, 5)

print(a)    # 4行5列数值是(100,200)随机整数矩阵
print(np.sqrt(a))   # 平方根
print(np.square(a))  # 平方
print(np.ceil(a))  # 向上取整
print(np.floor(a))  # 向下取整

print(a.sum())  # 求和
print(a.mean())  # 平均值
print(np.average(a))  # 平均值
print(a.std())  # 方差
print(a.var())  # 标准差
print(a.min())  # 最小值
print(a.max())  # 最大值
