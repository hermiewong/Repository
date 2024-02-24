import numpy as np
import matplotlib.pyplot as plt

N=np.random.poisson(10)
uv=np.array([[0,0]])
for i in range(N):
    uv=np.append(uv,[[np.random.rand(),np.random.rand()]],axis=0)
uv=uv[1:]
precede=np.array([[0,0]])
#index 0 precedes index 1
count=np.zeros(N)#number of precession for each element
for i in range(len(uv)):
    number=0
    for j in range(len(uv)):
        if i==j:
            continue
        if uv[i,0]<uv[j,0] and uv[i,1]<uv[j,1]:
            precede=np.append(precede,[[i,j]],axis=0)
            number+=1
    count[i]=number
        
precede=precede[1:]
link=np.array([[0,0]])
for i in range(len(precede)):
    firstindex=precede[i,0]
    secondindex=precede[i,1]
    uv1=uv[firstindex]
    uv2=uv[secondindex]
    notlink=0
    for j in range(len(uv)):
        uv3=uv[j]
        if firstindex==j or secondindex==j:
            continue
        if uv1[0]<uv3[0] and uv3[0]<uv2[0] and uv1[1]<uv3[1] and uv3[1]<uv2[1]:
            notlink=1
            break
    if notlink==1:
        continue
    if notlink==0:
        link=np.append(link,[precede[i]],axis=0)

link=link[1:]
print(len(precede)-len(link),'cuts made')

xt=np.array([[0,0]])
for i in uv:
    x=1/np.sqrt(2)*(i[0]-i[1])
    t=1/np.sqrt(2)*(i[0]+i[1])
    xt=np.append(xt,[[x,t]],axis=0)
xt=xt[1:]

plt.figure(1)
plt.scatter(uv[:,0],uv[:,1])
for i in link:
    plt.plot([uv[i[0],0],uv[i[1],0]],[uv[i[0],1],uv[i[1],1]])


plt.figure(2)
plt.xlabel('x')
plt.ylabel('t')
plt.grid()
plt.scatter(xt[:,0],xt[:,1])
for i in range(len(xt)):
    plt.text(xt[i,0],xt[i,1],i)
for i in link:
    plt.plot([xt[i[0],0],xt[i[1],0]],[xt[i[0],1],xt[i[1],1]])
plt.show()
