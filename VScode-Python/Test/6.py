import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x=np.linspace(-2,2)
y1=2*np.power(x,2)
y2=3*np.power(x,3)
y3=4*np.power(x,4)
matplotlib.rcParams['font.family'] = 'KaiTi'
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
plt.figure()
plt.title('函数曲线')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.plot(x,y1,'r:')
plt.plot(x,y2,'b-.')
plt.plot(x,y3,'y--')
plt.show()
