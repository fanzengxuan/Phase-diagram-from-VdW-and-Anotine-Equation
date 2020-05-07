import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def exp(a):
    return (2.71828**a)
def ln(a):
    return (np.log(a))

def Pvdw(T,v):
    a=0.55
    b=3.047926e-5
    p=8.314*T/(v-b)-a/v/v
    return p

def Objfun(T,v):
    R=8.314
    a=0.55
    b=3.047926e-5
    A=23.1963
    B=3816.44
    C=-46.13
    fun1=R*T/(v-b)-a/v/v
    fun2=exp(A-B/(T+C))
    return (fun1-fun2)**2

vList=list(np.linspace(3.047926e-5*3,1e-3,100))
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
plt.xlabel('v')
plt.ylabel('p')
#plt.show()
#plt.plot(TList,pList,'.')
#plt.show()
'''
TList_s=[]
pList_s=[]
vList_s=list(np.linspace(4.89936363500729e-5,3.047926e-5*2,5000))
print(len(vList_s))
for i in range(len(vList_s)):
    if i==0:
       sol=optimize.minimize(Objfun,522.7519775125323,args=(vList_s[i]),method='slsqp',options={'ftol':1e-25,'eps':1e-12})
    else:
       sol=optimize.minimize(Objfun,T,args=(vList_s[i]),method='slsqp',options={'ftol':1e-25,'eps':1e-12}) 
    T=sol.x[0]
    p=Pvdw(T,vList_s[i])
    #print(T,vList_s[i])
    pList_s.append(p)
    TList_s.append(T)
plt.plot(vList_s,pList_s)
plt.show()
'''
