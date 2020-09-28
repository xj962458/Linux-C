from math import *
a,b,c,x,y=[int(i) for i in (input("请输入a,b,c,x,y(用空格隔开)\n").split(' '))]
print((-b+sqrt(fabs(b*b-4*a*c)))/(2*a))
print((x**2+y**2)/2*a*a)
print(2*sin((x+y)/2)*cos((x-y)/2))
