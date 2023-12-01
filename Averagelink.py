import Sprinkle as sp
import matplotlib.pyplot as plt
import numpy as np

N=300
rho=50
avg=0
num=0
for i in range(N):
    causet=sp.sprinkle(rho)
    num+=causet.Num()
    rel=causet.relation()
    avg+=rel
avg/=N
num/=N
print('average relation=',avg)
print('average number of points=',num)
print('Expected relation=',rho**2/16*4)


# for i in np.arange(10,500,20,dtype=int):
#    causet=sp.sprinkle(i)
#    plt.scatter(i,causet.relation())
# plt.show()