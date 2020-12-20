import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,6.25,1000)
y1=np.sin(x)
y2=np.cos(x)
y3=np.sin(x*x)

plt.subplot(2,2,1)
plt.plot(x,y1,'r')
plt.xlim(0, 7)
plt.subplot(2,2,2)
plt.plot(x, y2, 'b--')
plt.xlim(0, 7)
plt.subplot(2,1,2)
plt.plot(x, y3, 'g--')
plt.xlim(0, 7)
plt.show()
