# Решение неоднородного уравнения Лапласа от одной переменной

import matplotlib.pyplot as plt

import numpy as np

X_0 = 0
X_1 = np.pi

U_0 = 0
U_1 = 1

H = 0.001

def f(x):
    # fanction
    fanction = np.sin(x)
    #
    return fanction

def F(i):
    return f(i*H)

n = int((X_1-X_0)/H) + 1

u = [i/10 for i in range(n)]
u[0] = U_0
u[-1] = U_1

def Alfa(i):
    return (i/(i+1))

def Omega(i):
    summ = 0
    for k in range(i-1):
        summ = summ + (k+1)*F(k)
    return summ

def Beta(i):
    rez = U_0 - Omega(i) * H**2
    return rez/(i+1)

for j in range(n-2):
    i = n-2-j
    u[i] = Alfa(i)*u[i+1] + Beta(i)

t = np.linspace(X_0, X_1, n)

plt.plot(t, u, color = 'blue', label = 'u')
plt.plot(t, f(t), color = 'green', label = 'f')
plt.legend()
plt.show()