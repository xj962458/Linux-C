from sympy import *

M = Matrix([1, 2, 3])

N = Matrix([4, 5, 6])

# 加法与减法

print("M+N:", M+N)
print("M-N:", M-N)


M1 = Matrix([[1, -1, 1], [2, 3, -2]])
N1 = Matrix([[1, 2], [2, 1], [1, 1]])

# 求乘法
print(M1*N1)

# 求逆矩阵
m = Matrix([[1, 3], [-2, 3]])
print(m**(-1))