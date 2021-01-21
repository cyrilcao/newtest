#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cyril
@file:matplotdemo.py
@time:2021/01/13/16:52
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# x = np.linspace(-1, 1, 100)
#
# y1 = x * 2 + 100
#
# y2 = x ** 2

# 创建一个画布

# figsize：设置画布的大小
#plt.figure(figsize=(5, 5))
#plt.plot(x, y1)

# 创建第二个画布
# plt.figure()
# plt.plot(x, y2)
#
# plt.show()


# # 绘制直方图
# x = np.arange(10)
# y = x ** 2 + 10
#
# # facecolor设置柱体的颜色
# # edgecolor设置边框的颜色
#
# plt.bar(x, y, facecolor='g', edgecolor='r')
#
# # 绘制翻转过来的直方图
# # plt.bar(x,-y)
#
# # 显示文字
# for x, y in zip(x, y):
#     plt.text(x, y, "{f}".format(f=y), ha="center", va='bottom')
# plt.show()

# 指定渲染环境
# % matplotlib
# notebook
# # %matplotlib inline

def update_points(num):
    point_ani.set_data(x[num], y[num])
    if num % 5 == 0:
        point_ani.set_marker("*")
        point_ani.set_markersize(12)
    else:
        point_ani.set_marker("o")
        point_ani.set_markersize(8)

    text_pt.set_position((x[num], y[num]))
    text_pt.set_text("x=%.3f, y=%.3f" % (x[num], y[num]))
    return point_ani, text_pt,


x = np.linspace(0, 2 * np.pi, 100)
y = np.cos(x)

fig = plt.figure(tight_layout=True)
plt.plot(x, y)
point_ani, = plt.plot(x[0], y[0], "ro")
plt.grid(ls="--")
text_pt = plt.text(4, 0.8, '', fontsize=16)

ani = animation.FuncAnimation(fig, update_points, np.arange(0, 100), interval=100, blit=True)

ani.save('C:\\360Downloads\\dosin_test3.gif', writer='imagemagick', fps=10)
plt.show()


