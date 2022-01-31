"""数组拼接"""
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[11, 12, 13], [14, 15, 16]])
print(a)
print(b)

# hstack水平方向拼接
r = np.hstack([a, b])
print(r)

# vstack垂直方向拼接
r = np.vstack((a, b))
print(r)

# concatenate沿着轴拼接  默认0-垂直方向
print("axis=0 默认情况:垂直方向拼接 vstack")
r1 = np.concatenate((a, b), axis=0)
r2 = np.concatenate((a, b))
print(r1)
print(r2)

# 二维数组 两个轴
print("axis=1 默认情况:水平方向拼接 hstack")
r3 = np.concatenate((a, b), axis=1)
print(r3)

# 三维数组 三个轴
print("axis=2 ")
a = np.arange(1, 13).reshape(1, 2, 6)
b = np.arange(101, 113).reshape(1, 2, 6)
print(a, a.shape)
print(b, a.shape)
print("三维 axis=0")
r1 = np.concatenate((a, b), axis=0)
print(r1, r1.shape)
print("三维 axis=1")
r2 = np.concatenate((a, b), axis=1)
print(r2, r2.shape)
print("三维 axis=2")
r3 = np.concatenate((a, b), axis=2)
print(r3, r3.shape)
