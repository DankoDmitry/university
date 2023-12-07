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

print(error_n_in_x(X_0, x_star, len(X_0)))



# t = np.linspace(0.1, 1.3, 100)

# plt.plot(t, P_n(X_0, t), color = 'blue', label = 'интеполяционный многочлен')
# plt.plot(t, Y(t), color = 'green', label = 'изначальная функция')
# plt.legend()
# plt.show()

# print(f"Разница между интерполяционным многочленом и искомой ф-й равна: {abs(Y(X_prime) - P_n(X_0, X_prime))}")

# t = np.linspace(0.1, 1.3, 100)

# ab = max(abs(Y(t) - P_n(X_0, t)))
# at = ab/max(abs(Y(t)))

# print (ab, at)
