import numpy as np
import matplotlib.pyplot as plt
from sympy import*

def exp(a):
    return (2.71828**a)

def Pvdw(T,v):
    a=0.5336
    b=3.047926e-5
    p=8.314*T/(v-b)-a/v/v
    return p

def Objfun(v,T):
    A=23.196
    B=3816.44
    C=-46.13
    a=0.554
    b=3.047926e-5  
    return (8.314*T/(v-b)-a/v**2-exp(A-B/(T+C)))

x=Symbol('x')
T=list(np.linspace(522.7519775125323,660,200))
vl=[]
vr=[]
pList=[]
for i in range(len(T)):
    Eqn=Objfun(x,T[i])
    sol=solve(Eqn,x)
    #print(sol)
    x1=re(sol[0])
    x2=re(sol[1])
    x3=re(sol[2])
    print(x1,x2,x3)
    if x1<7e-5:
        vl.append(x1)
        vr.append(x3)
        p=Pvdw(T[i],x1)
        pList.append(p)
    else:
        vl.append(x2)
        vr.append(x1)
        p=Pvdw(T[i],x2)
        pList.append(p)
print(pList)

plt.plot(vl,pList,)
plt.plot(vr,pList,)
plt.xlabel('v/m^3')
plt.ylabel('p/Pa')
plt.ylim(1.6e7,)
plt.xlim(0,0.0004)
plt.show()

