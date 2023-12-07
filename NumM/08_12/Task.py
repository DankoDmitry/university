# Решение неоднородного уравнения Лапласа от одной переменной

import matplotlib.pyplot as plt

import numpy as np

def f(x, y):
    return np.sin(x) + np.cos(y)

def f_2(x, y):
    return np.sin(x**2) + np.cos(y**2)


x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
y = x.copy().T
z_1 = f(x, y)
z_2 = f_2(x, y) + 5
 
fig = plt.figure()
 
# syntax for 3-D plotting
ax = plt.axes(projection='3d')
 
# syntax for plotting
ax.plot_surface(x, y, z_1, cmap='viridis', edgecolor='green')
ax.plot_surface(x, y, z_2, cmap='viridis', edgecolor='blue')
ax.set_title('Surface plot geeks for geeks')
plt.show()