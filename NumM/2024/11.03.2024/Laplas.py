import numpy as np
import matplotlib.pyplot as plt


def Messure(A, B):
    N = len(B)
    s = 0
    for i in range(N):
        for j in range(N):
            s = s + (abs(A[i,j] - B[i,j]))**2

    return np.sqrt(s)

def U_b(x):
    return np.sin(np.pi * x / 2)

def LaPlaS_Simp(L_b, U_b, D_b, l, h, E):
    N = int(l/h) + 1
    x_s = np.zeros((N,N))
    
    x_s[:, 0] = D_b
    for i in range(N):
        x_s[i, N-1] = U_b(i*h)
    x_s[0, :] = L_b
    # x_s[N, :] = R_b        -  По идее должно быть так, но нет - не должно
    
    x, y = x_s, x_s
    k = 0

    dif = 1

    while k < 1000 and dif > E:
        for i in range(1, N-1):
            for j in range(1, N-1):
                x[i,j] = (x[i-1,j]+x[i+1,j]+x[i,j-1]+x[i,j+1])/4
        x[-1] = x[-2]

        dif = Messure(x, y)
        if dif == 0: dif = 1
        y = x.copy()

        k+=1
    print(k)
    return (x)

h = 0.1
colorinterpolation = 50
colourMap = plt.cm.jet

x, y = np.linspace(0, 1, int(1/h) + 1), np.linspace(0, 1, int(1/h) + 1)
X, Y = np.meshgrid(x, y)
Z = LaPlaS_Simp(0, U_b, 0, 1, h, 0.0001)

ax = plt.axes(projection='3d')
ax.plot_surface(Y, X, Z, cmap='viridis', edgecolor='green')
ax.set_title('Contour of Temperature')
plt.show()
