import numpy as np 
import matplotlib.pyplot as plt
from random import *
import scipy.optimize as op

def sprinkle(L,avgN,d=2):
    N=np.random.poisson(avgN)
    position=[[0,L/2],[0,-L/2]]
    if d==2:
        for i in range(N-2):
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
                if prob(ti)>pi:
                    posneg=random()
                    if posneg>0.5:
                        t=ti
                    else:
                        t=-ti
            r=(L/2-ti)*np.sqrt(random())
            theta=random()*2*np.pi
            x=r*np.cos(theta)
            y=r*np.sin(theta)
            position.append([x,t,y])

    position=sorted(position,key=lambda x: x[1])
    return np.array(position)

def sprinkleADS(L,avgN,R_0,d=2):
    N=np.random.poisson(avgN)
    position=[]
    if d==2:
        A=np.log((L+2*R_0)/(2*R_0))+np.log((L+2*R_0)/(2*(L+R_0)))
        for i in range(N):
            rand1=random()
            rand2=random()
            posneg=random()
            ti=(L-np.sqrt(L**2-4*R_0*(R_0+L)*(np.exp(A*rand1)-1)))/2
            if posneg>0.5:
                t=-ti
            else:
                t=ti
            B=(R_0+ti)*(R_0+L-ti)/(L-2*ti)
            R=1/(1/(R_0+ti)-rand2/B)
            position.append([R,t])
    
    if d==3:
        def probt(t):
            return (t-L/2)**2/(R_0**2+R_0*L-t**2+t*L)
        def covert(t):
            return probt(0)*(1-2/L*t)
        def probR(R,t):
            return np.sqrt((t-L/2)**2-(R-(R_0+L/2))**2)/R**3

        for i in range(N):
            t=False
            while t==False:
                ti=L/2*(1-np.sqrt(1-random()))
                pi=random()*covert(ti)
                if probt(ti)>pi:
                    posneg=random()
                    if posneg>0.5:
                        t=ti
                    else:
                        t=-ti
            Rmax=5*(R_0+L/2)/4*(1-np.sqrt(1+24*((ti-L/2)/(R_0+L/2))**2)/5)
            C=probR(Rmax,ti)
            R=False
            while R==False:
                Ri=R_0+ti+2*random()*(L/2-ti)
                pi=random()*C
                if probR(Ri,ti)>pi:
                    R=Ri
            x=(random()-0.5)*2*np.sqrt((ti-L/2)**2-(R-(R_0+L/2))**2)
            position.append([R,t,x])


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
    L=4
    R_0=0.1
    N=10000

    #testing d=2 flat spacetime sprinkle and poisson nature of distribution
    # flat=sprinkle(L,N)
    # print(flat)
    # plt.scatter(flat[:,0],flat[:,1],marker='.')
    # plt.show()
    # l=0.2
    # x=np.linspace(-L/2+l/2,L/2-l/2,100)
    # num=[len(aleksandrov_interval_sample_ads(flat,l,[i,0])) for i in x]
    # plt.hist(num,bins=30)
    # plt.show()
    
    # #testing ADS distribution for d=2 in t, checks t transformation rule correctly generates desired t distribution
    # ads=sprinkleADS(L,N,R_0,2)
    # y,x,bin=plt.hist(ads[:,1],bins=30)
    # x=np.array([(x[i+1]+x[i])/2 for i in range(len(x)-1)])
    # def func(x,R,L,N):
    #     y=N*(1/(abs(x)+R)+1/(abs(x)-R-L))
    #     return y
    # fit=op.curve_fit(func,x,y,p0=[R_0,L,N/30])
    # x=np.linspace(-L/2,L/2,1000)
    # y=np.array([func(i,*fit[0]) for i in x])
    # plt.plot(x,y)
    # plt.show()

    # #show ADS distribution for d=2
    # ads=sprinkleADS(L,N,R_0,2)
    # plt.scatter(ads[:,0],ads[:,1],marker='.')
    # plt.show()

    #testing flat d=3 t distribution
    # flat=sprinkle(L,N,3)
    # plt.hist(flat[:,1],bins=30) #t distribution might have slight bias near t=0
    # plt.show()
    # plt.hist(flat[:,2],bins=30)
    # plt.show()
    # plt.hist(flat[:,0],bins=30)
    # plt.show()

    # #showing flat d=3 distribution
    # flat=sprinkle(L,N,3)
    # plt.scatter(flat[:,0],flat[:,2],marker='.')
    # plt.show()

    # # testing poisson for d=3 in flat spacetime
    # flat=sprinkle(L,N,3)
    # l=0.2
    # x=np.linspace(-L/2+l/2,L/2-l/2,100)
    # num=[len(aleksandrov_interval_sample_ads(flat,l,[i,0,0])) for i in x]
    # plt.plot(x,num)
    # plt.show()

    # #showing ADS d=3 distribution
    ads=sprinkleADS(L,N,R_0,d=3)
    plt.scatter(ads[:,0],ads[:,1],marker='.')
    plt.show()

    # #testing ADS d=3 intervals in t and x
    ads=sprinkleADS(L,N,R_0,d=3)
    l=0.2
    x=np.linspace(R_0+l/2,R_0+L-l/2,100)
    num=[len(aleksandrov_interval_sample_ads(ads,l,[i,0,0])) for i in x]
    def func(x,A):
        return A/x**3
    fit=op.curve_fit(func,x,num,p0=[N])
    plt.plot(x,num)
    plt.plot(x,func(x,fit[0]))
    plt.show()