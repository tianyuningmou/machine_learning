# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: matplotlib.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/7 上午9:52

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/7 上午9:52
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 一元函数图像
# 实例化作图变量
plt.figure()
# 图像标题
plt.title('single variable')
# x轴文本
plt.xlabel('x')
# y轴文本
plt.ylabel('y')
# x轴范围，y轴范围
plt.axis([0, 5, 0, 10])
# 是否绘制网格线
plt.grid(True)
# 生成10个点的随机向量
xx = np.linspace(0, 5, 10)
# 绘制图像
plt.plot(xx, 2*xx, 'r-')
# 展示图像
plt.show()

# 正弦函数图像
plt.figure()
plt.title('single variable')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-12, 12, -1, 1])
plt.grid(True)
xx = np.linspace(-12, 12, 1000)
# 绘制y=sin(x)图像，颜色green，形式为线条
plt.plot(xx, np.sin(xx), 'g-', label="$sin(x)$")
# 绘制y=cos(x)图像，颜色red，形式为虚线
plt.plot(xx, np.cos(xx), 'r--', label="$cos(x)$")
plt.legend()
plt.show()


# 绘制多轴图
def draw(plt):
    plt.axis([-12, 12, -1, 1])
    plt.grid(True)
    xx = np.linspace(-12, 12, 1000)
    plt.plot(xx, np.sin(xx), 'g-', label="$sin(x)$")
    plt.plot(xx, np.cos(xx), 'r--', label="$cos(x)$")
    plt.legend()


plt.figure()
# 两行两列中的第1张图
plt1 = plt.subplot(2, 2, 1)
draw(plt1)
# 两行两列中的第2张图
plt2 = plt.subplot(2, 2, 2)
draw(plt2)
# 两行两列中的第3张图
plt3 = plt.subplot(2, 2, 3)
draw(plt3)
# 两行两列中的第4张图
plt4 = plt.subplot(2, 2, 4)
draw(plt4)
plt.show()

# 绘制3D图像
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
# theta旋转角从-4pi到4pi，相当于两圈
theta = np.linspace(-4 * np.pi, 4 * np.pi, 500)
# z轴从下到上,从-2到2之间画100个点
z = np.linspace(0, 2, 500)
# 半径设置为z大小
r = z
# x和y画圆
x = r * np.sin(theta)
# x和y画圆
y = r * np.cos(theta)
ax.plot(x, y, z, label='curve')
ax.legend()
plt.show()

# 3D散点图
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
# 在0-5之间生成10个点的向量
xx = np.linspace(0, 5, 10)
# 在0-5之间生成10个点的向量
yy = np.linspace(0, 5, 10)
zz1 = xx
zz2 = 2*xx
zz3 = 3*xx
# o型符号
ax.scatter(xx, yy, zz1, c='red', marker='o')
# 三角型符号
ax.scatter(xx, yy, zz2, c='green', marker='^')
# 星型符号
ax.scatter(xx, yy, zz3, c='black', marker='*')
ax.legend()
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = X**2+Y**2
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.show()
