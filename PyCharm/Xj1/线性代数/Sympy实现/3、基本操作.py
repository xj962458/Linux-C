from sympy import *

m = Matrix([[1, -1], [3, 4], [0, 2]])
# 矩阵
print(m)

# 获得形状
print(m.shape)

# 获得单行与单列
print(m.row(0))
print(m.col(0))

# 删除行与列
m.row_del(0)
print("删除第一行后：", m)

m.col_del(0)
print("删除第一列后：", m)
print(m)

# 插入新的行与列
m2 = Matrix([[2, 3]])
print("m2:", m2)

m2 = m2.row_insert(1, Matrix([[0, 4]]))
print("插入新行后：", m2)

m2 = m2.col_insert(2, Matrix([9, 8]))
print("插入新列后：", m2)

# 求逆矩阵
print("其逆矩阵是：", m2.T)