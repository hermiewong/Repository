import numpy as np

def sprinkle(N,L,d,endpoint=False):
    Npoint=np.random.poisson(N)
    position=[]
    if endpoint==True:
        top=[0,L/2]
        bottom=[0,-L/2]
        for i in range(d-2):
            top.append(0)
            bottom.append(0)
        position.append(bottom)
        position.append(top)
    for i in range(N):
        x=np.random.rand(d)
        x[:]*=L
        x[:]-=L/2
        position.append(x)
    position=np.array(sorted(position,key=lambda x:x[1]))
    return position