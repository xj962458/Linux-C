a=[1,2,3,4,5,6,7,8]
#正序间隔输出
for i in range(0,len(a),2):
    print(a[i],end=' ')
else:
    print()
for i in range(1,len(a),2):
    print(a[i],end=' ')
print()

#逆序间隔输出
for i in range(len(a)-1,0,-2):
    print(a[i],end=' ')
else:
    print()
for i in range(len(a)-2,-1,-2):
    print(a[i],end=' ')

