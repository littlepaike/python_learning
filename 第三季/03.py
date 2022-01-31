import numpy as np

# range使用 range(start,end,step)
a = list(range(1, 10))
print(a)

b = list(range(10))
print(b)

c = list(range(1, 10, 3))
print(c)

# arange创建数组
a = np.arange(1, 11)
print(a)
# step
b = np.arange(1, 11, 2)
print(b)
# dtype
c = np.arange(10, 20, 2, dtype=float)
print(c)
