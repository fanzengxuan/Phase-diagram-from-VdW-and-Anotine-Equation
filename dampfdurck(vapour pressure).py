import numpy as np
import matplotlib.pyplot as plt

def exp(a):
    return (2.71828**a)

def Pressure(T):
    A=23.196
    B=3816.44
    C=-46.13
    return (exp(A-B/(T+C)))
def Volume(T,p):
    v=8.314*T/p
    return v

TList=np.linspace(273.16,647.4,20)

pList=[]
vList=[]
for i in range(len(TList)):
    
    p=Pressure(TList[i])
    print(p)
    pList.append(p)
    v=Volume(TList[i],p)
    vList.append(v)
    
plt.plot(TList,pList,'.')
plt.show()

