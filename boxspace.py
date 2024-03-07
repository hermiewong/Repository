import numpy as np
import matplotlib.pyplot as plt

def UV(N,L,endpoint=False):
    Npoisson=np.random.poisson(N)
    if endpoint==False:
        position=[]
    else:
        position=[[-L/2,-L/2],[L/2,L/2]]
    for i in range(Npoisson):
        position.append([np.random.random()-0.5,np.random.random()-0.5])
    position*=L

    return np.array(position)


def XT(N,L,endpoint=False):
    positionUV=UV(N,L,endpoint)
    position=[]
    for i in positionUV:
        t=(i[0]-i[1])/np.sqrt(2)
        x=(i[0]+i[1])/np.sqrt(2)
        position.append([t,x])
    position=sorted(position,key=lambda x:x[0])
    return np.array(position)


def LT(position,beta):
    newposition=[]
    gamma=1/np.sqrt(1-beta**2)
    for i in position:
        t=gamma*beta*i[0]-beta*i[1]
        x=gamma*beta*i[1]-beta*i[1]
        newposition.append([t,x])
    newposition=sorted(newposition,key= lambda x:x[0])
    return np.array(newposition)


set=XT(1000,1)
for i in set:
    plt.scatter(i[0],i[1])
plt.show()

LTset=LT(set,0.5)
for i in LTset:
    plt.scatter(i[0],i[1])
plt.show()
