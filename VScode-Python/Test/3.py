import time
# import numpy as np
import random

start = time.perf_counter()
a=[random.randint(0,101) for i in range(100000)]
x=0
print(a)
for i in a:
    x+=i*i
print(x)
end = time.perf_counter()
print("用时{}s".format(end-start))
