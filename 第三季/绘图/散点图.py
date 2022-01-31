import matplotlib.pyplot as plt
import numpy as np

# 绘制散点图
x = np.linspace(0, 10, 100)
sin_y = np.sin(x)

# 绘制正弦的曲线
plt.plot(x, sin_y,'o')
# plt.scatter(x,sin_y)
plt.show()