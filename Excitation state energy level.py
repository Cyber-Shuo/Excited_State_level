#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
#from matplotlib.font_manager import FontProperties
import numpy as np
#matplotlib.rc("font", family='Microsoft YaHei')
#my_font = FontProperties(fname=r"c:\windows\fonts\SimHei.ttf", size=12)

#创建画布
fig = plt.figure()

#使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)

#将绘图区对象添加到画布中
fig.add_axes(ax)

#通过set_axisline_style方法设置绘图区的底部及左侧坐标轴样式
#"-|>"代表实心箭头："->"代表空心箭头
ax.axis["bottom"].set_axisline_style("-|>")
ax.axis["left"].set_axisline_style("-|>")

#通过set_visible方法设置绘图区的顶部及右侧坐标轴隐藏
ax.axis["top"].set_visible(False)
ax.axis["right"].set_visible(False)

plt.axhline(y=10,c="r",ls="--",lw=1)
plt.axhline(y=30,c="y",ls="--",lw=1)
plt.axhline(y=50,c="gray",ls="--",lw=1)
plt.axhline(y=90,c="g",ls="--",lw=1)
plt.axhline(y=110,c="b",ls="--",lw=1)

plt.text(410,10,'$\sigma$',rotation=0,color='r')
plt.text(410,30,'$\pi$',rotation=0,color='y')
plt.text(410,50,'n',rotation=0,color='gray')
plt.text(410,110,'$\sigma^*$',rotation=0,color='b')
plt.text(410,90,'$\pi^*$',rotation=0,color='g')

#plt.quiver(200,10,0,100,angles='xy',scale=1,scale_units='xy')
#plt.quiver(230,50,0,60,angles='xy',scale=1,scale_units='xy')
#plt.quiver(240,30,0,60,angles='xy',scale=1,scale_units='xy')
#plt.quiver(310,50,0,40,angles='xy',scale=1,scale_units='xy')

plt.annotate('$\sigma$ to $\sigma^*$', xy=(200,9), xytext=(180,113), arrowprops=dict(arrowstyle='<->'))
plt.annotate('n to $\sigma^*$', xy=(240,49), xytext=(220,113), arrowprops=dict(arrowstyle='<->'))
plt.annotate('$\pi$ to $\pi^*$', xy=(250,29), xytext=(230,93), arrowprops=dict(arrowstyle='<->'))
plt.annotate('n to $\pi^*$', xy=(310,49), xytext=(290,93), arrowprops=dict(arrowstyle='<->'))

plt.ylabel('Energy')
plt.xlabel('Wavelength(nm)')
plt.title('transition level')

plt.xticks([100,200,300,400])
plt.yticks([])

plt.show()
