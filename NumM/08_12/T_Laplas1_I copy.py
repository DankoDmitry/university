# Решение однородного уравнения Лапласа от одной переменной работает нормально


import matplotlib.pyplot as plt

import numpy as np


X_0 = 0
X_1 = np.pi

U_0 = 1
U_1 = 0

H = 0.001

n = int((X_1-X_0)/H) + 1

print (1/H)

def f(x):
    # fanction
    fanction = x
    #
    return x/x-1

def F(i):
    return f(i*H)

u = [i/10 for i in range(n)]
# print (u)
u[0] = U_0
u[-1] = U_1
# print (u)

def Alfa(i):
    return (i/(i+1))

def Omega(i):
    summ = 0
    for k in range(n-1):
        summ = summ + (k+1)*F(k)
    return summ

def Beta(i):
    rez = U_0
    return rez/(i+1)

for j in range(n-2):
    i = n-2-j
    u[i] = Alfa(i)*u[i+1] + Beta(i)

# print (u)


t = np.linspace(X_0, X_1, n)

plt.plot(t, u, color = 'blue', label = 'u')
plt.plot(t, f(t), color = 'green', label = 'f')
plt.legend()
plt.show()