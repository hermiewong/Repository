import numpy as np

def sprinkle(N,L,d,R_0,endpoint=False,half=True):
    """
    sprinkle into AdS cube of size L
    endpoint: adds a point to t=L/2,-L/2 and R=R_0 if true, not included in Npoint
    half: if true only sprinkles into L/2 in R direction
    """
    Npoint=np.random.poisson(N)
    position=[]
    if endpoint=True:
        top=[R_0,L/2]
        bottom=[R_0,-L/2]
        for i in range(d-2):
            top.append(0)
            bottom.append(0)
        position.append(bottom)
        position.append(top)
    if half==True:
        for i in range(Npoint):
            x=np.random.rand(d)
            x[1:]*=L
            x[1:]-=L/2
            x[0]=(R_0**(1-d)*(1-x[0])+(R_0+L/2)**(1-d)*x[0])**(-1/(d-1))
            position.append(x)
    else:
            x=np.random.rand(d)
            x[1:]*=L
            x[1:]-=L/2
            x[0]=(R_0**(d-1)/(1-x[0]))**(1/(d-1))
            position.append(x)
    position=np.array(sorted(position,key=lambda x: x[1]))
    return position