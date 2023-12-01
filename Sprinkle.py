import numpy as np
import matplotlib.pyplot as plt

class sprinkle:
    """
    density,Num=True/False(returns number of sprinkled points if True)
    """
    def __init__(self,density=100,Num=0):
        self.density=density
        self.__uv=np.array([[0,0]])
        N=np.random.poisson(density)
        for i in range(N):
            self.__uv=np.append(self.__uv,[[np.random.rand(),np.random.rand()]],axis=0)
        self.__uv=self.__uv[1:]
        self.__precede={}
        for i in range(len(self.__uv)):
            ith=[]
            for j in range(len(self.__uv)):
                if i==j:
                    continue
                if self.__uv[i,0]<self.__uv[j,0] and self.__uv[i,1]<self.__uv[j,1]:
                    ith.append(j)
            self.__precede[i]=ith

        self.__link={}
        for i in self.__precede:
            ith=[]
            for j in self.__precede[i]:
                notlink=0
                uv1=self.__uv[i]
                uv2=self.__uv[j]
                for k in self.__precede[i]:
                    uv3=self.__uv[k]
                    if j==k:
                        continue
                    if uv1[0]<uv3[0] and uv3[0]<uv2[0] and uv1[1]<uv3[1] and uv3[1]<uv2[1]:
                        notlink=1
                        break
                if notlink==1:
                    continue
                if notlink==0:
                    ith.append(j)
            self.__link[i]=ith
        self.__xt=np.array([[0,0]])
        for i in self.__uv:
            x=1/np.sqrt(2)*(i[0]-i[1])
            t=1/np.sqrt(2)*(i[0]+i[1])
            self.__xt=np.append(self.__xt,[[x,t]],axis=0)
        self.__xt=self.__xt[1:]
        if Num==1:
            print("Sprinkled",len(self.__uv),"points")

    def __repr__(self):
        return "sprinkle(%s)"%self.density
    
    def __str__(self):
        relation=0
        for i in self.__precede:
            relation+=len(self.__precede[i])
        avgrela=relation/len(self.__precede)
        link=0
        for i in self.__link:
            link+=len(self.__precede[i])
        avglink=link/len(self.__link)
        return "Sprinkle density=%s, Sprinkled point=%s, number of relation=%s, average relation=%s, number of link=%s, average link=%s" %(self.density,len(self.__uv),relation,avgrela,link,avglink)

    def xt(self):
        return self.__xt
    
    def uv(self):
        return self.__uv
    
    def plot(self,style=0):
        """
        plot(style=0)
        style: 0 plots in uv coordinate, 1 plots in __xt coordinate
        """
        if style==0:
            plt.scatter(self.__uv[:,0],self.__uv[:,1])
            for i in self.__link:
                for j in self.__link[i]:
                    plt.plot([self.__uv[i,0],self.__uv[j,0]],[self.__uv[i,1],self.__uv[j,1]])
        if style==1:
            plt.scatter(self.__xt[:,0],self.__xt[:,1])
            for i in self.__link:
                for j in self.__link[i]:
                    plt.plot([self.__xt[i,0],self.__xt[j,0]],[self.__xt[i,1],self.__xt[j,1]])
    
    def relation(self):
        return self.__precede
    
    def link(self):
        return self.__link
    
class sprinkle2():
    """
    removes one sprinkled point and places it at (0,0). Homogeneity of poisson
    distribution should mean that the resulting sprinkling is also poisson
    """
    def __init__(self,density=100,Num=0):
        self.density=density
        self.__uv=np.array([[0,0]])
        N=np.random.poisson(self.density)
        N-=1
        for i in range(N):
            self.__uv=np.append(self.__uv,[[np.random.rand(),np.random.rand()]],axis=0)
        self.__precede={}
        for i in range(len(self.__uv)):
            ith=[]
            for j in range(len(self.__uv)):
                if i==j:
                    continue
                if self.__uv[i,0]<self.__uv[j,0] and self.__uv[i,1]<self.__uv[j,1]:
                    ith.append(j)
            self.__precede[i]=ith

        self.__link={}
        for i in self.__precede:
            ith=[]
            for j in self.__precede[i]:
                notlink=0
                uv1=self.__uv[i]
                uv2=self.__uv[j]
                for k in self.__precede[i]:
                    uv3=self.__uv[k]
                    if j==k:
                        continue
                    if uv1[0]<uv3[0] and uv3[0]<uv2[0] and uv1[1]<uv3[1] and uv3[1]<uv2[1]:
                        notlink=1
                        break
                if notlink==1:
                    continue
                if notlink==0:
                    ith.append(j)
            self.__link[i]=ith
        self.__xt=np.array([[0,0]])
        for i in self.__uv:
            x=1/np.sqrt(2)*(i[0]-i[1])
            t=1/np.sqrt(2)*(i[0]+i[1])
            self.__xt=np.append(self.__xt,[[x,t]],axis=0)
        self.__xt=self.__xt[1:]
        if Num==1:
            print("Sprinkled",len(self.__uv),"points")

    def __repr__(self):
        return "sprinkle(%s)"%self.density
    
    def __str__(self):
        relation=0
        for i in self.__precede:
            relation+=len(self.__precede[i])
        avgrela=relation/len(self.__precede)
        link=0
        for i in self.__link:
            link+=len(self.__precede[i])
        avglink=link/len(self.__link)
        return "Sprinkle density=%s, Sprinkled point=%s, number of relation=%s, average relation=%s, number of link=%s, average link=%s" %(self.density,len(self.__uv),relation,avgrela,link,avglink)

    def xt(self):
        return self.__xt
    
    def uv(self):
        return self.__uv
    
    def plot(self,style=0):
        """
        plot(style=0)
        style: 0 plots in uv coordinate, 1 plots in __xt coordinate
        """
        if style==0:
            plt.scatter(self.__uv[:,0],self.__uv[:,1])
            for i in self.__link:
                for j in self.__link[i]:
                    plt.plot([self.__uv[i,0],self.__uv[j,0]],[self.__uv[i,1],self.__uv[j,1]])
        if style==1:
            plt.scatter(self.__xt[:,0],self.__xt[:,1])
            for i in self.__link:
                for j in self.__link[i]:
                    plt.plot([self.__xt[i,0],self.__xt[j,0]],[self.__xt[i,1],self.__xt[j,1]])
    
    def relation(self):
        return self.__precede
    
    def link(self):
        return self.__link

    def maximal_chain(self,start=0,end=100):
        """
        start:index of point in self.__link we wish to start our chain from
        end:maximum number of points added in our maximal chain
        """
        init=[]
        for i in self.__link[start]:
            init.append([start,i])
        list=[[0],[len(init)]]
        update=1
        update2=1
        while end>update2 and not update==0:
            update=0
            # init2=[]
            for i in init:
                nextindex=i[-1]
                nextlist=self.__link[nextindex]
                if len(nextlist)==0:
                    # init2.append(i)
                    continue
                else:
                    for index,j in enumerate(nextlist):
                        if index==0:
                            i.append(j)
                        else:
                            copy=i.copy()
                            copy[-1]=j
                            init.append(copy)
                        # init2.append(copy)
                        update+=1
            # init=init2
            update2+=1
        return init

    # def plotchain(self,start=0,end=100):
    #     chainlist=self.maximal_chain(start,end)
    #     plt.scatter(self.__xt[:,0],self.__xt[:,1])
    #     for i in chainlist:
    #         for j in range(len(i)-1):
    #             plt.plot([self.__xt[i[j],0],self.__xt[i[j+1],0]],[self.__xt[i[j],1],self.__xt[i[j+1],1]])
    # A lot of repeated plotting makes this very slow. Don't use


class sprinklem(sprinkle2):
    """
    sprinkle class with swerve using momentum model
    """
    def __init__(self,density=100):
        sprinkle2.__init__(self,density,Num=0)
    
    def Lorentz(self,index1,index2): #Takes index of two points in self.__xt and Lorentz transform so that one is on top of the other
        """
        index1 is past element
        index2 is future element
        boost is automatically calculated
        return transform only of points with relation with future point.
        new frame transformed to have past at origin and THEN past and future on vertical axis
        """
        if index1==index2:
            newframe={index1:np.array([0,0])}
            for i in self.relation()[index1]:
                newframe[i]=self.xt()[i]
            return newframe
        past=self.xt()[index1]
        future=self.xt()[index2]
        vector=future-past
        if vector[1]<0:
            raise Exception("the future is the past")
        elif vector[1]<abs(vector[0]):
            raise Exception("spacelike vector")
        velocity=vector[0]/vector[1]
        newframe={index2:np.array([0,0])}#translate past to origin
        for i in self.relation()[index2]:
            point=self.xt()[i]
            translate=point-future
            xprime=(translate[0]-velocity*translate[1])/np.sqrt(1-velocity**2)
            tprime=(translate[1]-translate[0]*velocity)/np.sqrt(1-velocity**2)
            newframe[i]=np.array([xprime,tprime])
        return newframe

    def forgetting(self,time,index,frame): #index is index of point we are finding the forgetting element for
        list=[]
        for i in self.relation()[index]:
            x,t=frame[i]
            if t**2-x**2<time**2:
                list.append(i)
        return list

    def trajectory(self,time,end,testing=0): #end is end time in original frame
        """
        time:forgetting time
        end: space-like hypersurface with t=end in the original frame at which we stop the trajectory
        The last point will be one point beyond the hypersurface
        """
        index1=0
        index2=0
        traject=[index1]#create list of index to store trajectory
        starttime=self.xt()[index1,1]
        while starttime<end:#start while loop here,repeat until t of next point in original xt is beyond end
            newframe=self.Lorentz(index1,index2)#lorentz transform to have next point in origin and new and old point on vertical axis
            possible=self.forgetting(time,index2,newframe)#find points within forgetting time of the origin
            if len(possible)==0:
                print('no possible point left')
                x=np.linspace(-0.7,0.7,500)
                y=np.sqrt(time**2+x**2)+self.xt()[index2,1]
                cone=abs(x)+self.xt()[index2,1]
                x+=self.xt()[index2,0]
                plt.plot(x,y)
                plt.plot(x,cone)
                break
            for i,index in enumerate(possible):#find index of point with lowest abs(x) within forgetting time
                if i==0:
                    newindex=index
                elif abs(newframe[newindex][0])>abs(newframe[index][0]):
                    newindex=index

            if testing==1:
                x=np.linspace(-0.7,0.7,500)
                y=np.sqrt(time**2+x**2)+self.xt()[index2,1]
                cone=abs(x)+self.xt()[index2,1]
                x+=self.xt()[index2,0]
                plt.plot(x,y)
                plt.plot(x,cone)

            index1,index2=index2,newindex#update index for next loop
            traject.append(newindex)#add index to trajectory list
            starttime=self.xt()[newindex,1]#update starttime to reflect time of next point in the original frame
        return traject
    
    def plottraject(self,time,end,testing=0):
        traject=self.trajectory(time,end,testing)
        plt.scatter(self.xt()[:,0],self.xt()[:,1],s=2)
        plt.plot(self.xt()[traject,0],self.xt()[traject,1])




class sprinklen(sprinkle2):
    """
    sprinkle class with swerve using forgetting number model
    """
    def __init(self,density=100):
        sprinkle2.__init__(self,density,Num=0)


class sprinkle3():
    def __init__(self,density=100,Number=100):
        self.list=[]
        for i in range(Number):
            self.list.append(sprinkle2(density))
    

        

    

