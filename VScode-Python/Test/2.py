import time
import numpy as np

start=time.perf_counter()
a=np.random.randint(0,101,100000)
a=a^2
x=0
for i in a:
    x+=i
print(x)
end = time.perf_counter()
print("用时{}s".format(end-start))
