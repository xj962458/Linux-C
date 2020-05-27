from sympy import *

# 单位矩阵
m1 = eye(3)
print(latex(m1))

# 零矩阵
m2 = zeros(3, 4)
print(latex(m2))

# 一矩阵
m3 = ones(3, 4)
print(latex(m3))

# 对角矩阵
m4 = diag([1, 2, 3])
print(latex(m4))
