import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point1  = np.array([0,0,0])
normal1 = np.array([1,-2,1])

point2  = np.array([0,-4,0])
normal2 = np.array([0,2,-8])

point3  = np.array([0,0,1])
normal3 = np.array([-4,5,9])

# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set
d1 = -np.sum(point1*normal1)# dot product
d2 = -np.sum(point2*normal2)# dot product
d3 = -np.sum(point3*normal3)# dot product

# create x,y
xx, yy = np.meshgrid(range(30), range(30))

# calculate corresponding z
z1 = (-normal1[0]*xx - normal1[1]*yy - d1)*1./normal1[2]
z2 = (-normal2[0]*xx - normal2[1]*yy - d2)*1./normal2[2]
z3 = (-normal3[0]*xx - normal3[1]*yy - d3)*1./normal3[2]

# plot the surface
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1, color='blue')
plt3d.plot_surface(xx,yy,z2, color='yellow')
plt3d.plot_surface(xx,yy,z3, color='cyan')
plt.show()