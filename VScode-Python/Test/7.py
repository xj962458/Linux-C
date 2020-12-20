import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = np.linspace(0, 5,1000)
y=np.cos(2*np.pi*x)
matplotlib.rcParams['font.family'] = ''
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
plt.figure()
plt.grid()
plt.xlim(-1,6)
plt.ylim(-2.0,2.0)
plt.plot(x,y,'r--')
plt.title('正弦波实例$y=cos(2Πx)$')
plt.xlabel('横轴：时间')
plt.ylabel('纵轴:振幅')
plt.show()
