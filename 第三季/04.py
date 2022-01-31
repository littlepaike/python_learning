"""随机创建数组"""
import numpy as np


def randomTest():
    # random创建一维数组
    a = np.random.random(size=5)
    print(a)

    # 创建二维数组
    b = np.random.random(size=(3, 4))
    print(b)

    # 创建三维数组
    c = np.random.random(size=(2, 3, 4))
    print(c)


# randomTest()


# 随机整数
def randomIntTest():
    # 生成0-5随机整数 一维
    a = np.random.randint(6, size=10)
    print(a)

    # 生成5-10之间的随机整数 二维
    b = np.random.randint(5, 11, size=(4, 3))
    print(b)

    # 5-10随机数  三维
    c = np.random.randint(5, 11, size=(2, 4, 3))
    print(c)

    # dtype使用
    d = np.random.randint(10, size=5, dtype=np.int64)
    print(d.dtype)


# randomIntTest()

# 创建标准的正态分布 期望0 方差1
def randnTest():
    """正态分布"""
    a = np.random.randn(4)
    print(a)

    # 创建二维的
    b = np.random.randn(2, 3)
    print(b)

    # 创建三维
    c = np.random.randn(2, 3, 4)
    print(c)


# randnTest()

# 创建指定的方差和正太分布
def normalTest():
    a = np.random.normal(size=5)  # loc=0.0 scale=1.0
    print(a)

    # 指定期望方差
    b = np.random.normal(loc=2, scale=3, size=(3, 4))
    print(b)


normalTest()
