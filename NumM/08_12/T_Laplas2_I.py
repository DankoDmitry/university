# Решение неоднородного уравнения Лапласа от двух переменных

import numpy as np
import matplotlib.pyplot as plt

N = 20
Tau = 10**(-6)

def f(r):
    return np.sin((5*r*np.pi/2)/N)

lenX = lenY = N 
delta = 1

r = np.linspace(0, N, N)

Ttop = f(r)
Tbottom = 0
Tleft = 0
Tright = 0

Tguess = 10

colorinterpolation = 50
colourMap = plt.cm.jet

X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

T = np.empty((lenX, lenY))
T.fill(Tguess)

print(np.shape(Ttop))
T[(lenY-1):, :] = Ttop
T[:1, :] = Tbottom
T[:, (lenX-1):] = Tright
T[:, :1] = Tleft

S = np.empty((N, N)) 
S_1 = np.empty((N, N)) 
S_an = np.empty((lenX, lenY))
S_an.fill(Tguess)

def E(x):
    x = x
    return np.exp(2.5*x*np.pi)

def analit(r, z):
    r = r/N
    z = z/N
    return ((E(z) - E(-1*z))/(E(1) - E(-1))) * np.sin(2.5*r*np.pi)

Error = 1
while Error > Tau:
    Error = 0
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):
            T[i, j] = 0.25 * (T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])
            e = abs(T[i, j]-S[i,j])
            S[i,j] = T[i, j]
            if Error < e: Error = e

    print (Error)



plt.title("Contour of Temperature")
plt.contourf(X, Y, T, colorinterpolation, cmap=colourMap)
plt.colorbar()
plt.show()

# print("")

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, T, cmap='viridis', edgecolor='green')
ax.set_title('Contour of Temperature')
plt.show()


Error_an = 0

for i in range(1, lenX-1, delta):
    for j in range(1, lenY-1, delta):
        e_an = abs(S[i, j]-analit(i, j))
        S_an[i, j] = analit(i, j)
        if Error_an < e_an: Error_an = e_an

print("wiuvnakjvnkjnk        ", Error_an)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, S_an, cmap='viridis', edgecolor='green')
ax.set_title('Contour of Temperature')
plt.show()
