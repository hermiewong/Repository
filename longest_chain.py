def link(relation): # assumes there is a point at top and bottom of interval, and relations is sorted in time order
    link=relation.copy()
    #for bottom point we know top point will not be link so
    #we bypass this point with a separate loop
    candidate=relation[0]
    ith_link=[candidate[0]]#closest in time with a relation is always a link
    for index,value in enumerate(candidate[1:-1]):
        append=0
        for k in candidate[0:index+1]:#don't need to check the current candidate and any future candidates
            if value in relation[k]:
                append+=1
                break
        if append==0:
            ith_link.append(value)
    trim_relation=relation.copy()
    trim_relation.pop(0)
    trim_relation.pop(len(trim_relation))
    link[0]=ith_link
    for i,j in enumerate(trim_relation):#last element has no relations
        candidate=relation[j]
        ith_link=[candidate[0]]#closest in time with a relation is always a link
        for index,value in enumerate(candidate[1:]):
            append=0
            for k in candidate[0:index+1]:
                if value in relation[k]:
                    append+=1
                    break
            if append==0:
                ith_link.append(value)
        link[j]=ith_link
    return link

def longest_chain(link,cycle=20):
    """
    link: dictionary of links
    """
    maximal=[]
    for i in link[0]:
        maximal.append([0,i])
    flow=1
    count=0
    while flow>0:
        count+=1
        flow=0
        if count==cycle:
            count=0
            endpoint=[]
            maximal_copy=[]
            for i in maximal:
                if not i[-1] in endpoint:
                    endpoint.append(i[-1])
                    maximal_copy.append(i)
            maximal=maximal_copy
        maximal_copy=[]
        for i in maximal:
            if link.get(i[-1])==None:
                continue
            for j in link[i[-1]]:
                element=i.copy()
                element.append(j)
                maximal_copy.append(element)
                flow+=1
        if flow!=0:
            maximal=maximal_copy
    return maximal
            
if __name__=='__main__':
    import ADS2 as ads
    N=2000
    L=100
    d=2
    cycle=1
    flat=ads.sprinkle(L,N,d)
    relation={}
    for i,base in enumerate(flat):
        ith=[]
        for j,check in enumerate(flat[i+1:]):
            
            # if not len(base)==len(check):
            #     raise Exception("index of different position not matching")
            vector=check-base

            # true as conformal transform doesn't change lightcone so its just
            # Minkowski - hence can use usual proper time definition
            tausq=vector[1]**2 - vector[0]**2 - sum(vector[2:]**2)
            
            if tausq>0:
                ith.append(j+i+1)

        relation[i]=ith
    # print(relation)
    import time
    t0=time.time()
    lonk=link(relation)
    t1=time.time()
    long=longest_chain(lonk,cycle)
    t2=time.time()
    print('Link time=',t1-t0)
    print('longest chain time=',t2-t1)
    print("longest chains length:",len(long[0]))
    volume=L**2/2
    print('Number of points sprinkled:',len(flat))
    # print('volume=',volume)
    density=len(flat)/volume
    ldiscrete=density**(-1/d)
    print('density=',density)
    print('discreteness length=',ldiscrete)
    # print('tau/ldiscrete=',L/ldiscrete)
    print('longest*ldiscrete/tau=',len(long[0])*ldiscrete/L)
    print('mdcd**1/d=',2*(1/2)**(1/d))
