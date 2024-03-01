import numpy as np
import matplotlib.pyplot as plt

def W(s: complex, a: complex,b: complex,c: complex,d: complex,e: complex,g: complex):
    I_1 = a*s + b
    I_2 = c*s**3 + d*s**2 + e*s + g
    return (I_1/I_2)


t = np.linspace(-50, 50, 10000)

arr = [1,3,1,6,3,2]

s = [complex(0,i) for i in t]
u = [W(i,arr[0],arr[1],arr[2],arr[3],arr[4],arr[5]).real for i in s]
v = [W(i,arr[0],arr[1],arr[2],arr[3],arr[4],arr[5]).imag for i in s]

plt.plot(u, v, color = 'blue', label = 'АФЧХ')
plt.scatter(-1, 0, color = 'r', label = '(-1, 0)')

plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Task е')
plt.legend()
plt.show()

