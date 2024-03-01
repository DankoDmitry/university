import matplotlib.pyplot as plt
import numpy as np

# вариант 9

def f(x):
    return x/(x**2 + 9)
X_0 = 0
X_1 = 2

h = 0.5

def Rectangle(F, X_0, X_1, h):
    n = int((X_1 - X_0)/h)
    arr = [i*h for i in range(n+1)]
    Square = 0
    for i in range(n):
        Square = Square + h*F((arr[i]+arr[i+1])/2)
    return Square
print(Rectangle(f, X_0, X_1, h))

def Trapezoid(F, X_0, X_1, h):
    n = int((X_1 - X_0)/h)
    arr = [i*h for i in range(n+1)]
    Square = 0
    for i in range(n):
        Square = Square + h*(F(arr[i])+F(arr[i+1]))/2
    return Square
print(Trapezoid(f, X_0, X_1, h))

def Simpson(F, X_0, X_1, h):
    n = int((X_1 - X_0)/h)
    arr = [i*h for i in range(n+1)]
    Square = 0
    for i in range(1, n+1):
        Square = Square + h*(F(arr[i-1]) + 4*F((arr[i-1]+arr[i])/2) + F(arr[i]))/6
    return Square
print(Simpson(f, X_0, X_1, h))

# def Error(F, F_An, X_0, X_1, h):
#     print(

print (np.log(13/9)/2)

t = np.linspace(X_0, X_1, 100)

plt.plot(t, f(t), color = 'blue', label = 'АФЧХ')
plt.xlim(0, 2)
plt.ylim(0, 2)
plt.show()
