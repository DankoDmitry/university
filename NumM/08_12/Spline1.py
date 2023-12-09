import matplotlib.pyplot as plt

import numpy as np

def f(x):
    return 1/x

# a)
X_star = 0.8
X = [0.1, 0.5, 0.9, 1.3]

h = 0.4


n = int((X[-1]-X[0])/h) + 2

ef = [f(X[i]) for i in range(n)]



def F(i):
    return (ef[i-1] - 2*ef[i] + ef[i+1])/h**2

def Alfa(i):
    if i == 0: return -1/4
    else: return (-1)/(Alfa(i-1)+4)

def Beta(i):
    return (18*F(i) - 2)/(3*Alfa(i-1) + 12)

m = [0.] * (n-1)

for j in range(n-3):
    i = n-3-j
    m[i] = Alfa(i)*m[i+1] + Beta(i)


def g(i, x):
    I_1 = m[i-1]*(X[i] - x)**3/(6*h)
    I_2 = m[i]*(x - X[i-1])**3/(6*h)
    I_3 = (ef[i-1] - m[i-1]*h**2/6)*(X[i]-x)/h
    I_4 = (ef[i] - m[i]*h**2/6)*(x-X[i-1])/h

    return I_1 + I_2 + I_3 + I_4

def G(x):
    if x < 0.5: return g(1, x)
    else: return g(2, x)

t = np.linspace(X[0], X[-1], 100)

l = [t[i] for i in range(len(t))]
Ge = [G(l[i]) for i in range(len(t))]

print (ef)

plt.plot(t, Ge, color = 'blue', label = 'g')
plt.plot(t, f(t), color = 'green', label = 'f')
plt.legend()
plt.show()

ab = max(abs(g(2, t) - f(t)))
print(ab)