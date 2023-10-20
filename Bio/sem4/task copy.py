from scipy.integrate import odeint

import matplotlib.pyplot as plt

import numpy as np

from scipy.integrate import odeint

r = 0.1
K = 1000

y0 = [10, 200, 700]

t = np.linspace(0, 200, 2000)

epsilon = 0.001

tau = 0.1

def pend(y, t, r, K):
    N = y
    dydt = r*N*(1-N/K)
    return dydt

sol = odeint(pend, y0, t, args=(r, K))

analit = (y0[0] * np.e ** (r*t)) / (1 - y0[0]/K + (y0[0] * np.e ** (r*t)) / K)


def f(y):
    return r*y - r*y*y/K

def f_prime(y):
    return r - r*2*y/K

def F(y_n, y_n_past):
    return y_n - tau*f(y_n) - y_n_past

def F_prime(y_n):
    return 1 - tau*f_prime(y_n)

rez = [y0[0]]

for i in range(1999):
    k = rez[i]
    ko = k - F(k, rez[i])/F_prime(k)
    while abs(ko - k) > epsilon:
        k = ko
        ko = k - F(k, rez[i])/F_prime(k)
        
    new = ko
    rez.append(new)


plt.plot(t, rez, 'g', label='implicit')
plt.plot(t, analit, 'b', label='analit')
plt.legend()
plt.show()


analit_arr = [analit[i] for i in range(999)]

abs_delta_y = 0
for i in range(999):
    abs_delta_y = max(abs(rez[i] - analit[i]), abs_delta_y)
relativ_delta_y = max(abs(rez - analit)/analit)


print(f'abs_delta_y = {abs_delta_y} \nrelative_delta_y = {relativ_delta_y}')