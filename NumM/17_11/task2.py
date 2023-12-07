import matplotlib.pyplot as plt

import numpy as np


X_0 = [0.1, 0.5, 0.9, 1.3]
# X_1 = [0.1, 0.5, 1.1, 1.3]

X_prime = 0.8
x_star = X_prime

def Y(x): return 1/x

def Fi(X, x, i):
    prod = 1
    for j in range(0, len(X)):
        if i != j:
            prod = prod*(x - X[j])/(X[i] - X[j])
    return prod

def P_n(X, x):
    rez = 0
    for i in range(0, len(X)):
        rez = rez + Y(X[i])*Fi(X, x, i)
    return rez

def Omyga_n(X, x_star):
    rez = 1
    for i in range(0, len(X)):
        rez = rez*(x_star - X[i])
    return rez

def fac(k):
    if k == 0: return 1
    else: return fac(k-1)*k

def Y_prime_n(x, n):
    return ((-1)**n)*(fac(n))/x**(n+1)

def error_n_in_x(X, x_star, n):
    t = np.linspace(0.1, 1.3, 100)
    return max(Y_prime_n(t, n)) * abs(Omyga_n(X, x_star)) / fac(n)

def Dif_f(mass):
    if len(mass) == 2: return (Y(mass[-1]) - Y(mass[0]))/(mass[-1] - mass[0])
    else:
        arr_1 = mass[1:]
        arr_2 = mass[:-1]
        return (Dif_f(arr_1) - Dif_f(arr_2))/(mass[-1] - mass[0])

mass = [x_star] + X_0

print(Dif_f(mass)*Omyga_n(X_0, x_star))

# print(error_n_in_x(X_0, x_star, len(X_0)))

# mass = [1,2,3,4,5]
# arr = mass[1:]
# print(arr)