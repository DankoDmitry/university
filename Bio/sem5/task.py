from scipy.integrate import odeint
from scipy.integrate import solve_ivp

import matplotlib.pyplot as plt


import numpy as np

u0 = [0.5, 1.1, 0.7]
v0 = [0.5, 2, 1]


gamma = .2
t0 = 0
tf = 400
st = .1

def lotkavolterra(t, z):
    u, v = z
    return [u*(1-v), gamma*v*(u - 1)]

sol = [solve_ivp(lotkavolterra, [t0, tf], [u0[i], v0[i]], max_step=st) for i in range(3)]

t = np.arange(t0-st, tf, st)


fig, ax = plt.subplots(3, 2, sharex=True)

for i in range(3):
    ax[i, 0].plot(t, (sol[i].y)[0], color="blue", label='жертва')
    ax[i, 0].plot(t, (sol[i].y)[1], color="red", label='жертва')

    ax[i, 1].plot((sol[i].y[0]), (sol[i].y)[1])
    ax[i, 0].legend()

fig.set_figheight(15)
fig.set_figwidth(15)

plt.show()