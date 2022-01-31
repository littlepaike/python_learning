import numpy as np

# 创建一维数组
a = np.array([1, 2, 3, 4])
print(a)
print(type(a))

# 创建二维数组
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
print(type(b))

# 创建三维数组
c = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(c)
print(type(c))

# array函数中dtype的使用
d = np.array([3, 4, 5], dtype=float)
print(d)
print(type(d))

# ndmin
e = np.array([6, 7, 8, 9], dtype=float, ndmin=3)
print(e)
