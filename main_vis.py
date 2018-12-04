from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def norm(data, dataTest):
	dataTestValue = ( dataTest - np.min(data) ) / ( np.max(data) - np.min(data) )
	return ( data - np.min(data) ) / ( np.max(data) - np.min(data) ) , np.clip( dataTestValue , 0, 1)

fig = plt.figure()
ax = fig.gca(projection='3d')

n = 100
x1 = np.array([60,70,80,100,40])
x2 = np.array([165,160,165,155,175])

beratBadan = float(input('Berat Badan : '))
tinggiBadan = float(input('Tinggi Badan : '))

x1, beratBadan = norm(x1, beratBadan)
x2, tinggiBadan = norm(x2, tinggiBadan)

x1 = np.append(x1, beratBadan)
x2 = np.append(x2, tinggiBadan)

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].

for c, m, index in [('r', 'o', 0), ('b', '^',1), ('g', 's',2)]:
    if index == 0 :
        xs = x1[0:3]
        ys = x2[0:3]
    elif index == 1 :
        xs = x1[3:5]
        ys = x2[3:5]
    else :
        xs = x1[5:6]
        ys = x2[5:6]
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
