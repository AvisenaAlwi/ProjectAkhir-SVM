from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def norm(data):
	return ( data - np.min(data) ) / ( np.max(data) - np.min(data) )

fig = plt.figure()
ax = fig.gca(projection='3d')

n = 100
datax = np.array([60,70,80,100,40, 90])
datay = np.array([165,160,165,155,175, 155])
# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].

datax = norm(datax)
datay = norm(datay)
for c, m, index in [('r', 'o', 0), ('b', '^',1), ('g', 's',2)]:
    if index == 0 :
        xs = datax[0:3]
        ys = datay[0:3]
    elif index == 1 :
        xs = datax[3:5]
        ys = datay[3:5]
    else :
        xs = datax[5:6]
        ys = datay[5:6]
    zs = (xs * ys) ** 2
    ax.scatter(xs, ys, zs, c=c, marker=m)

X = np.arange(-0.1, 1.1, 0.1)
Y = np.arange(-0.1, 1.1, 0.1)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
for i in range(len(R)) :
  R[i].fill(0.01)
Z = R
ax.plot_surface(X, Y, Z,linewidth=0, antialiased=True, alpha=0.5)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
