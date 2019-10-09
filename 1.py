import numpy as np
from scipy.optimize import fmin
import matplotlib.pyplot as plt

a = np.linspace(-5,5,100)
x,y = np.meshgrid(a,a)
z = 8*x*y -4*(x**2)*y -2*x*(y**2) + (x**2)*(y**2)
fig = plt.figure()
ax = fig.add_subplot(111)

cpf = ax.contourf(x,y,z, 10)

x,y = 0.5,0.5

Argument = [x,y]

max = 4

def optimize(parameters):
    x,y = parameters[0],parameters[1]
    Polynomial = 8*x*y-4*(x**2)*y-2*x*(y**2)+(x**2)*(y**2)
    minmax = np.abs(Polynomial - max)
    return minmax



optimization = fmin(optimize,Argument,xtol=0.001)


print(optimization)
plt.show()

