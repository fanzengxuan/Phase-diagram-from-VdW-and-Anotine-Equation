import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def exp(a):
    return (2.71828**a)
def ln(a):
    return (np.log(a))

def Pvdw(T,v):
    a=0.66565
    b=3.047926e-5
    p=8.314*T/(v-b)-a/v/v
    return p

def Objfun(T,v):
    R=8.314
    a=0.66565
    b=3.047926e-5
    A=23.1963
    B=3816.44
    C=-46.13
    fun1=R*T/(v-b)-a/v/v
    fun2=exp(A-B/(T+C))
    return (fun1-fun2)**2

vList=list(np.linspace(1.25e-4,1e-3,500))
#vList=vList+list(np.linspace(1.0e-4,1.3e-4,100))
vList.reverse()
print(vList)

TList=[]
pList=[]
for i in range(len(vList)):
    if i==0:
        sol=optimize.minimize(Objfun,500,args=(vList[0]),method='slsqp',options={'ftol':1e-25,'eps':1e-12})
    else:
        sol=optimize.minimize(Objfun,T,args=(vList[i]),method='slsqp',options={'ftol':1e-25,'eps':1e-12})
    #print(sol)
    T=sol.x[0]
    p=Pvdw(T,vList[i])
    print(T,vList[i])
    pList.append(p)
    TList.append(T)
plt.plot(vList,pList)
plt.show()
plt.plot(TList,pList,'.')
plt.show()

