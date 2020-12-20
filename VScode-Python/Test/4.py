import time
import numpy as np
import random

start = time.perf_counter()
a = [random.randint(0, 101) for i in range(100000)]
x = 0
for i in a:
    x += i*i
print(x)
end = time.perf_counter()
print("列表用时{:5f}s".format(end-start))

start = time.perf_counter()
a = np.random.randint(0, 101, 100000)
a=np.square(a)
print(a.sum())
end = time.perf_counter()
print("numpy用时{:5f}s".format(end-start))
