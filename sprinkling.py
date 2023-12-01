#%%
import numpy as np
import matplotlib.pyplot as plt
params= {
   'axes.labelsize': 16,
   'font.size': 18,
   'legend.fontsize': 18,
   'xtick.labelsize': 16,
   'ytick.labelsize': 16,
   'figure.figsize': [10, 6] 
   }
plt.rcParams.update(params)


n=500
N=(n*2)**2
L=32
A=L**2
epsilon=A/N
if epsilon>1:
    raise Exception
counter=0
occurrence=0
for i in range(-n,n):
    for j in range(-n,n):
        random=np.random.random()
        if random<epsilon:
            if type(occurrence)==int:
                occurrence=np.array([[i,j]])
                counter+=1
            elif len(occurrence)>=1:
                occurrence=np.append(occurrence,[[i,j]],0)
                counter+=1
#%%
gridlabel=np.linspace(-L/2,L/2,9)
gridpoint=np.linspace(-n,n,9)
#plt.grid()
plt.figure(1)
plt.subplot(1,2,1)
plt.xlabel('Original')
plt.xticks(gridpoint,gridlabel)
plt.yticks(gridpoint,gridlabel)
plt.xlim(-1*n/3,1*n/3)
plt.ylim(-2*n/3,2*n/3)
plt.scatter(occurrence[:,0],occurrence[:,1],marker='x')
print(len(occurrence),A)
#%%Lorentz boost
def boost(array,beta):
    gamma=1/np.sqrt(1-beta**2)
    lorentz=np.array([[gamma,-beta*gamma],[-beta*gamma,gamma]])
    boosted=0
    for i in array:
        if type(boosted)==int:
            boosted=np.array([np.matmul(lorentz,i)])
        elif len(boosted)>=1:
            boosted=np.append(boosted,[np.matmul(lorentz,i)],0)
    return boosted

boosted=boost(occurrence,0.5)

plt.subplot(1,2,2)
plt.xlabel(r'Lorentz boosted by $\beta$=0.5')
plt.xticks(gridpoint,gridlabel)
plt.yticks(gridpoint,gridlabel)
plt.xlim(-1*n/3,1*n/3)
plt.ylim(-2*n/3,2*n/3)
plt.scatter(boosted[:,0],boosted[:,1],marker='x')


# %%
uniform=np.array([[L/2,L/2]])
for i in np.arange(-L/2,L/2+1):
    for j in np.arange(-L/2,L/2+1):
        uniform=np.append(uniform,[[i,j]],0)
uniform=uniform[1:]


plt.figure(2)
plt.subplot(1,2,1)
plt.xticks(gridlabel,gridlabel)
plt.yticks(gridlabel,gridlabel)
plt.xlim(-1*L/3/2,1*L/3/2)
plt.ylim(-2*L/3/2,2*L/3/2)
plt.xlabel('Original')
plt.scatter(uniform[:,0],uniform[:,1],marker='x')
# %%
newuniform=boost(uniform,0.5)
plt.figure(2)
plt.subplot(1,2,2)
plt.xticks(gridlabel,gridlabel)
plt.yticks(gridlabel,gridlabel)
plt.xlim(-1*L/3/2,1*L/3/2)
plt.ylim(-2*L/3/2,2*L/3/2)
plt.xlabel(r'Lorentz boosted by $\beta$=0.5')
plt.scatter(newuniform[:,0],newuniform[:,1],marker='x')
plt.show()
# %%
