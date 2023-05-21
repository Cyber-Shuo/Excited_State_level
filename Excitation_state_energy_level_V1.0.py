import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np

fig = plt.figure()
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

# use set_axisline_style set axis style
ax.axis["bottom"].set_axisline_style("-|>")
ax.axis["left"].set_axisline_style("-|>")

# use set_visible hide top and right axis
ax.axis["top"].set_visible(False)
ax.axis["right"].set_visible(False)

# set energy level witj different color
plt.axhline(y=10, c="r", ls="--", lw=1)
plt.axhline(y=30, c="y", ls="--", lw=1)
plt.axhline(y=50, c="gray", ls="--", lw=1)
plt.axhline(y=90, c="g", ls="--", lw=1)
plt.axhline(y=110, c="b", ls="--", lw=1)

# label energy level
plt.text(410, 10, '$\sigma$', rotation=0, color='r')
plt.text(410, 30,' $\pi$', rotation=0, color='y')
plt.text(410, 50, 'n', rotation=0, color='gray')
plt.text(410, 110, '$\sigma^*$', rotation=0, color='b')
plt.text(410, 90, '$\pi^*$', rotation=0, color='g')

# make annotate
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
