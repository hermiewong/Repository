import numpy as np 
import matplotlib.pyplot as plt
from random import *
import scipy.optimize as op

def sprinkle(L,avgN,d=2):
    N=np.random.poisson(avgN)
    position=[]
    if d==2:
        for i in range(N):
            rand1=random()
            rand2=random()
            if rand1<0.5:#t negative
                t=L/2*(-1+np.sqrt(2*rand1))
                x=(rand2-0.5)*(L+2*t)
            elif rand1>=0.5:#t positive
                t=L/2*(1-np.sqrt(2*(1-rand1)))
                x=(rand2-0.5)*(L-2*t)
            position.append([x,t])


    if d==3:
        def prob(t):
            return 6/L-24*t/L**2+24*t**2/L**3
        def cover(t):
            return 6/L-12/L**2*t
        for i in range(N):
            #sprinkle in t using rejection method:
            t=False
            while t==False:
                ti=L/2*(1-np.sqrt(1-random()))
                pi=random()*cover(ti)
                if prob(ti)<pi:
                    t=ti
            position.append([0,t])

    position=sorted(position,key=lambda x: x[1])
    return np.array(position)

def sprinkleADS(L,avgN,R_0,d=2):
    N=np.random.poisson(avgN)
    position=[]
    if d==2:
        A=2*(np.log((L+2*R_0)/(2*R_0))+np.log((L+2*R_0)/(2*(L+R_0))))
        position=[]
        for i in range(N):
            rand1=random()
            rand2=random()
            if rand1>0.5:
                t=(L-np.sqrt(L**2-4*R_0*(R_0+L)*(np.exp(A*(rand1-0.5))-1)))/2
                B=(R_0+t)*(R_0+L-t)/(L-2*t)
                R=1/(1/(R_0+t)-rand2/B)
                position.append([R,t])
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
    R_0=0.1
    N=10000

    #testing d=2 flat spacetime sprinkle and poisson nature of distribution
    # flat=sprinkle(L,N)
    # print(flat)
    # plt.scatter(flat[:,0],flat[:,1],marker='.')
    # plt.show()
    # l=0.2
    # x=np.linspace(-L/2+l/2,L/2-l/2,100)
    # num=[len(aleksandrov_interval_sample_ads(flat,l,[0,i])) for i in x]
    # plt.hist(num,bins=30)
    # plt.show()

    ads=sprinkleADS(L,N,R_0,2)
    y,x,bin=plt.hist(ads[:,1],bins=30)
    print(x,y)
    x=np.array([(x[i+1]+x[i])/2 for i in range(len(x)-1)])

    def func(x,R,L,N):
        y=N*(1/(x+R)+1/(x-R-L))
        return y
    fit=op.curve_fit(func,x,y,p0=[R_0,L,N/30])
    x=np.linspace(0,1,1000)
    y=np.array([func(i,*fit[0]) for i in x])
    plt.plot(x,y)
    plt.show()

    # ads=sprinkleADS(L,N,R_0,2)
    # plt.scatter(ads[:,0],ads[:,1],marker='.')
    # plt.show()
