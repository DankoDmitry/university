import matplotlib.pyplot as plt
import numpy as np

def main():
    def f(x, y): return x**2 + (y-1)**2

    def grad_f(x, y, h=0.1): return [(f(x + h, y) - f(x - h, y))/(2*h), (f(x, y + h) - f(x, y - h))/(2*h)]

    def Iter(f, grad_f, Bound, N): 
        z = np.zeros((3, N))
        z[:,0] = [Bound, Bound, f(Bound, Bound)]
        for i in range(1, N):
            x, y = -grad_f(z[0, i-1], z[1, i-1])[0], -grad_f(z[0, i-1], z[1, i-1])[1]
            a, b = z[0, i - 1] + x, z[1, i - 1] + y
            while f(a, b) > f(z[0, i-1], z[1, i-1]):
                a = a/2
                b = b/2
            
            z[0, i] = a
            z[1, i] = b
        
        return z

    h = 0.01
    colorinterpolation = 50
    colourMap = plt.cm.jet

    x, y = np.linspace(-3, 3, int(1/h) + 1), np.linspace(-3, 3, int(1/h) + 1)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    
    # print(Iter(f, grad_f, 3, 20))

    ax = plt.axes(projection='3d')
    ax.plot_surface(Y, X, Z, cmap='viridis', edgecolor='green')
    ax.set_title('Contour of Temperature')
    ax.plot(Iter(f, grad_f, 3, 20)[0], Iter(f, grad_f, 3, 20)[1], Iter(f, grad_f, 3, 20)[2])
    plt.show()

main()