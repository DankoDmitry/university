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

t = np.linspace(0, 100, 1000)


from scipy.integrate import odeint
sol = odeint(pend, y0, t, args=(r, K))


analit = (y0[0] * np.e ** (r*t)) / (1 - y0[0]/K + (y0[0] * np.e ** (r*t)) / K)



def X_Implicit_Y(y, tau, r, K, n0):
    if y == 0:
        return n0
    else:
        b = K * (1-tau*r)/(tau*r)
        c = K/(tau*r)
        D = b**2 + y*4*c
        return (-b + np.sqrt(D))/2
m = [10]


for i in range(999):
    m.append(X_Implicit_Y(m[i], 0.1, r, K, y0[0]))

# print(m)


plt.plot(t, m, 'g', label='implicit')
plt.plot(t, analit, 'b', label='analit')
plt.legend()
plt.show()
analit_arr = [analit[i] for i in range(999)]

abs_delta_y = 0
for i in range(999):
    abs_delta_y = max(abs(m[i] - analit[i]), abs_delta_y)
relativ_delta_y = max(abs(m - analit)/analit)


print(f'abs_delta_y = {abs_delta_y} \nrelative_delta_y = {relativ_delta_y}')