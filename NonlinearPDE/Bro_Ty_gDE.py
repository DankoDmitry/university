import numpy as np
import matplotlib.pyplot as plt

k = 9
N = 10
h = 1/((k+1))
t = np.arange(0, 1, (1/((k+1)*N)))

def u0(x):
    #return - x**2/2 + x/2
  m = ((1-np.cosh(1))/np.sinh(1))
  return np.cosh(x) + m*np.sinh(x) - 1

c = np.zeros(N+1)
epsilon = h/100


for i in range (N):
  c[i] = u0(i*h)
'''
def Suck_my_balls(cum_in_my_mounth):
  res=0
  fuck = 0
  ahahaah= 0
  for i in range(1,N):
    fuck += cum_in_my_mounth[i]**2 - cum_in_my_mounth[i]*cum_in_my_mounth[i-1] - cum_in_my_mounth[i]*cum_in_my_mounth[i+1]
    ahahaah += (2*cum_in_my_mounth[i]**2 + cum_in_my_mounth[i]*cum_in_my_mounth[i-1] + cum_in_my_mounth[i]*cum_in_my_mounth[i+1] )/6  + cum_in_my_mounth[i]
  res+= fuck/h + ahahaah*h +1/2 - h/2 
  return res

def Anek_pro_shlapy(cum_in_my_mounth,i):
  res = (cum_in_my_mounth[i]*2 - cum_in_my_mounth[i-1] - cum_in_my_mounth[i+1]) + h*h*(4*cum_in_my_mounth[i] + cum_in_my_mounth[i-1] + cum_in_my_mounth[i+1] )/6  + h*h
  return res
'''


def grad(cum_in_my_mounth):
  res = np.zeros(N+1)
  for i in range(1,N):
    res[i] = (cum_in_my_mounth[i]*2 - cum_in_my_mounth[i-1] - cum_in_my_mounth[i+1]) + h*h*(4*cum_in_my_mounth[i] + cum_in_my_mounth[i-1] + cum_in_my_mounth[i+1] )/6  
    res[i] += i*(h**3)*np.sin(c[i]) - h*h
  return res


def Suck_my_balls(cum_in_my_mounth):
  res=0
  fuck = 0
  ahahaah= 0
  for i in range(1,N):
    fuck += cum_in_my_mounth[i]**2 - cum_in_my_mounth[i]*cum_in_my_mounth[i-1] - cum_in_my_mounth[i]*cum_in_my_mounth[i+1]
    ahahaah += (2*cum_in_my_mounth[i]**2 + cum_in_my_mounth[i]*cum_in_my_mounth[i-1] + cum_in_my_mounth[i]*cum_in_my_mounth[i+1] )/6  - cum_in_my_mounth[i] 
    ahahaah += - h*cum_in_my_mounth[i]*np.cos(cum_in_my_mounth[i])
  res+= fuck/h + ahahaah*h +1/2 -h/2
  return res
'''
def Horse_porn(cum_in_my_mounth):
  res = 0
  res+= integ(lambda x: integrand_u_prime_squared(x,c), 0,1, n)
  res+= integ(lambda x: integrand_G(x,c), 0, 1, n )
  res-= integ(lambda x: integrand_fu(x,c), 0, 1, n )
  return res

def BBC(yes, YES):
  res = 0
  res += integ(lambda x: integrand_prime(x, yes, YES),YES*h - h, YES*h+h, n )
  res += integ(lambda x: integrand_g(x, yes, YES), YES*h - h, YES*h+h, n )
  res -= integ(lambda x: integrand_f(x,  YES), YES*h - h, YES*h+h, n )
  return res

def domination(female):
  res = np.zeros(N+1)
  for YES in range(1,N):
    res[YES] = BBC(female, YES)
  return res

'''
iter = 0
w = 1




while iter < 1000 and w>epsilon:
  iter+=1
  temp = c - w*grad(c)
  
  if Suck_my_balls(temp) < Suck_my_balls(c):        #СЮДА НЕ ЗАХОДИТ!!!!!!!
    print('hehe')
    c = temp.copy()
  else:
    w *= 0.5

print(Suck_my_balls(c))
print(iter)

# plt.plot(t, [u(c,i) for i in t], color = 'green')
# plt.plot(t, [u0(x) for x in t], color = 'red')

# plt.show()