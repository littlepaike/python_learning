import matplotlib.pyplot as plt
import numpy as np

# 绘制10种大小 100种颜色的散点图
# 创建x
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)
size = np.random.rand(10) * 1000
color = np.random.rand(100)
# 绘制散点图
plt.scatter(x, y, sizes=size, c=color, alpha=0.7)
plt.show()
