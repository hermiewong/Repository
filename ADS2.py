import numpy as np 
import matplotlib.pyplot as plt
from random import *


def sprinkle(L,avgN,d=2):
    N=np.random.poisson(avgN)
    position=[]
    for i in range(N):
        posneg=choice([1,0])
        rand=random()
        if posneg: #t positive
            t=L/2*(1-np.sqrt(rand))
        elif not posneg: #t negative
            t=L/2*(-1+np.sqrt(rand))
        

        position.append([t])
    return np.array(position)


if __name__ == "__main__":
    L=2
    # x=np.linspace(-L-0.1,L+0.1,100)
    y=sprinkle(L,10000)
    print(y)
    plt.hist(y,bins=50)
    plt.show()