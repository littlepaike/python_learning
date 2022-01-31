import numpy as np

# 通过reshape将一维数组修改为二三维数组
a = np.arange(1, 25)
print(a)

# 一转二
b = a.reshape(3, 8)
print(b)

# 一转三
c = a.reshape(2, 3, 4)
print(c)

# 一转二
bb = np.reshape(a, (3, 8))
print(bb)

# 一转三
cc = np.reshape(a, (2, 3, 4))
print(cc)

# 多维转为一维
a = bb.reshape(-1)
print(a)

b = bb.ravel()
print(b)

a = bb.flatten()
print(a)
