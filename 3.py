from scipy.optimize import fsolve
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

def equation_solver(x):
    return (3*x+10)


solution= fsolve(equation_solver,0)

print(solution)

fig = plt.figure()
ax = fig.gca(projection='3d')


X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)

Z = X*Y

colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[x, y] = colortuple[(x + y) % len(colortuple)]

surf = ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0)


ax.set_zlim(-5, 5)
ax.w_zaxis.set_major_locator(LinearLocator(6))

plt.show()
