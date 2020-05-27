from sympy import *

M = Matrix([[3, -2,  4, -2], [5,  3, -3, -2], [5, -2,  2, -2], [5, -2, -3,  3]])

P, D = M.diagonalize()

print('矩阵M')
print(M)

print('矩阵P')
print(P)

print('矩阵D')
print(D)

print("P*D*P**-1")
print(P*D*P**-1)

