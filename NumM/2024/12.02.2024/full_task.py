import numpy as np
import matplotlib.pyplot as plt

h = 0.1
X = 1
x_0 = 0
y_0 = 1.5

N = int((X - x_0)/h)                                        # 10 при h = 0.1

def f(y,x):
    return (-1 * y + np.exp(x))                             # y' = f(y,x)

def Y(x):
    return (np.exp(x)/2 + np.exp(-x))                       # Аналитическое решение

E = np.zeros((2,4))                                         # Масссив для ошибок

x = np.array([int((x_0 + i*h)*N)/N for i in range(N+1)])    # Координаты по x

y = np.zeros((4, N+1))                                      # Ввели массив значений
y[:,0] = y_0                                                # Дали начальные условия

    # 0 - для Эйлера
    # 1 - для Рунге-Курта 3-го порядка (не то, что на доске, а тот, что на лекции)
    # 2 - для Рунге-Курта 3-го порядка
    # 3 - для Рунге-Курта 4-го порядка

def Error(Num_met, Mass=E, N = N, y = y, x = x):
    m = 0
    s = 0
    for i in range(N + 1):
        temp = abs(y[Num_met, i] - Y(x[i]))
        if temp > m: m = temp
        s = s + (abs(y[Num_met, i] - Y(x[i])))**2

    Mass[0, Num_met] = m
    Mass[1, Num_met] = np.sqrt(s)

def Euler(N = N, h = h, Y = Y, f = f, x = x, y = y, Er = E):
    k = np.zeros((4,N + 1))

    for i in range(N): 
        k[0,i] = h*f(y[0,i],x[i])
        y[0,i+1] = y[0,i] + k[0,i]

    Error(0, Er, N = N, y = y, x = x)

def Runge_Kutta_method_3_lecture(N = N, h = h, Y = Y, f = f, x = x, y = y, Er = E):
    k = np.zeros((4,N + 1))

    for i in range(N): 
        k[0,i] = h*f(y[1, i], x[i])
        k[1,i] = h*f(y[1, i] + k[0, i]/2, x[i] + h/2)
        k[2,i] = h*f(y[1, i] + k[1, i]/2, x[i] + h/2)
        dy = (k[0, i] + 2*k[1, i] + k[2, i])/4
        y[1, i+1] = y[1, i] + dy

    Error(1, Er, N = N, y = y, x = x)

def Runge_Kutta_method_3_sem(N = N, h = h, Y = Y, f = f, x = x, y = y, Er = E):
    k = np.zeros((4,N + 1))

    for i in range(N): 
        k[0,i] = h*f(y[2, i], x[i])
        k[1,i] = h*f(y[2, i] + k[0, i]/3, x[i] + h/3)
        k[2,i] = h*f(y[2, i] + 2*k[1, i]/3, x[i] + 2*h/3)
        dy = (k[0, i] + 3*k[2, i])/4
        y[2, i+1] = y[2, i] + dy

    Error(2, Er, N = N, y = y, x = x)

def Runge_Kutta_method_4(N = N, h = h, Y = Y, f = f, x = x, y = y, Er = E):
    k = np.zeros((4,N + 1))

    for i in range(N): 
        k[0,i] = h*f(y[3, i], x[i])
        k[1,i] = h*f(y[3, i] + k[0,i]/2, x[i] + h/2)
        k[2,i] = h*f(y[3, i] + k[1,i]/2, x[i] + h/2)
        k[3,i] = h*f(y[3, i] + k[2,i], x[i] + h)
        dy = (k[0,i] + 2*k[1,i] + 2*k[2,i] + k[3,i])/6
        y[3, i+1] = y[3, i] + dy

    Error(3, Er, N = N, y = y, x = x)

Euler()
Runge_Kutta_method_3_lecture()
Runge_Kutta_method_3_sem()
Runge_Kutta_method_4()

h_1 = 0.05
X = 1
x_0 = 0
y_0 = 1.5

N_1 = int((X - x_0)/h_1)                                       

def f(y,x):
    return (-1 * y + np.exp(x))                          

def Y(x):
    return (np.exp(x)/2 + np.exp(-x))                     

E_1 = np.zeros((2,4))                                      

x_1 = np.array([int((x_0 + i*h_1)*N_1)/N_1 for i in range(N_1+1)])  

y_1 = np.zeros((4, N_1+1))                                  
y_1[:,0] = y_0                                          

Euler(N = N_1, h = h_1, x = x_1, y = y_1, Er = E_1)
Runge_Kutta_method_3_lecture(N = N_1, h = h_1, x = x_1, y = y_1, Er = E_1)
Runge_Kutta_method_3_sem(N = N_1, h = h_1, x = x_1, y = y_1, Er = E_1)
Runge_Kutta_method_4(N = N_1, h = h_1, x = x_1, y = y_1, Er = E_1)


# print(x, x_1)
# print(y, "\n")
# print(y_1)

# print(E)
# print(E_1)

P = np.zeros((2,4))
for i in range(2):
    for j in range(4):
        P[i,j] = np.log2(E[i,j]/E_1[i,j])

print(P)