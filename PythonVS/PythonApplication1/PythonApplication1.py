# 3、求e的值
def fac(x):
    if (x == 1 or x == 0):
        return x
    else:
        return x * fac(x - 1)
i = s = 1
while 1 / fac(i) >= pow(10, -99):
    s = s + 1 / fac(i)
    i += 1
s = s + 1 / fac(i)
print("e等于{}".format(s))