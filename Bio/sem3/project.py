from scipy.integrate import odeint

import matplotlib.pyplot as plt

import numpy as np
def pend(y, t, r, K):
    N = y
    dydt = r*N*(1-N/K)
    return dydt
r = 0.1
K = 1000

y0 = [10, 200, 700]

t = np.linspace(0, 200, 100)

sol = odeint(pend, y0, t, args=(r, K))
analit = (y0[0] * np.e ** (r*t)) / (1 - y0[0]/K + (y0[0] * np.e ** (r*t)) / K)
plt.plot(t, sol[:, 0], 'r', label='N(0) = 10')
plt.plot(t, analit, 'g', label='N(0) = 10')
# plt.show()

abs_delta_y = max(abs(sol[:, 0] - analit))
relativ_delta_y = max(abs(sol[:, 0] - analit)/analit)


print(f'abs_delta_y = {abs_delta_y} \nrelative_delta_y = {relativ_delta_y}')

