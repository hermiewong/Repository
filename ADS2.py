import numpy as np 
import matplotlib.pyplot as plt
from random import *


def sprinkle(L,avgN,d=2):
    N=np.random.poisson(avgN)
    position=[]
    if d==2:
        for i in range(N):
            posneg=choice([1,0])
            rand=random()
            if posneg: #t positive
                t=L/2*(1-np.sqrt(rand))
                x=(random()-0.5)*(L/2-t)
            elif not posneg: #t negative
                t=L/2*(-1+np.sqrt(rand))
                x=(random()-0.5)*(L/2+t)
            position.append([t,x])
    position=sorted(position,key=lambda x: x[1])
    return np.array(position)

def aleksandrov_interval_sample_ads(points, l, interval_centre):
    # points - the numpy array with all the points. Needs to be sorted by the
    #          time coordinate.
    # l is the height of the double cone, end to end.
    # interval centre - yet again, numpy array with the interval centre.
    # Expected coordinate order: R, t, x_i,

    point_subset = set()
    points_copy = np.copy(points)

    # Centre time coordinate.
    t_c = interval_centre[1]

    i = 0
    
    # True when reached a point higher than the tip of the double cone
    # As points are ordered by the time coordinate, going over the top
    # means the next points need not be checked.
    over_time = False

    while i < len(points_copy) and not over_time:
        #ith p point.
        pi = points_copy[i]
        ti = pi[1]
    
        diffs = pi - interval_centre

        delta_t = np.abs(diffs[1])

        if delta_t < 0.5 * l:
            
            r_max = l/2 - delta_t
            r_max_squared = r_max**2
            r_squared = diffs[0]**2 + sum(diffs[2:]**2)

            if r_squared < r_max_squared:
                point_subset.add(i)

        elif ti > t_c:
            over_time = True

        i += 1

    return point_subset

if __name__ == "__main__":
    L=2
    # x=np.linspace(-L-0.1,L+0.1,100)
    y=sprinkle(L,5000)
    print(y)
    plt.scatter(y[:,0],y[:,1],marker='.')
    plt.show()
    l=0.2
    x=np.linspace(-L/2+l/2,L/2-l/2,100)
    num=[len(aleksandrov_interval_sample_ads(y,l,[i,0])) for i in x]
    plt.hist(num,bins=30)
    plt.show()