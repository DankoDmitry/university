import matplotlib.pyplot as plt

import numpy as np

N = 21

n = [1/(i+1) for i in range(N//2)]
n_1 = [n[-i-1] for i in range(N//2)]
n_2 = [n[i]* (-1) for i in range(N//2)]

X = n_2 + n_1
X_0 = n + n_1
print(X)
X_prime = 0.8

def Y(x): return abs(x)

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

t = np.linspace(-1, 1, 20)

plt.plot(t, P_n(X, t), color = 'blue', label = 'интеполяционный многочлен')
# plt.plot(t, Y(t), color = 'green', label = 'изначальная функция')
plt.legend()
plt.show()

# print(f"Разница между интерполяционным многочленом и искомой ф-й равна: {abs(Y(X_prime) - P_n(X_0, X_prime))}")

# t = np.linspace(0.1, 1.3, 100)

# ab = max(abs(Y(t) - P_n(X_0, t)))
# at = ab/max(abs(Y(t)))

# print(ab, at)
# print(f"Ln(x) = {P_n(X, X_prime)}")
