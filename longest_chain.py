def link(relation): # assumes there is a point at top and bottom of interval, and relations is sorted in time order
    link={}
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

    link[0]=ith_link
    for i,j in enumerate(relation):#last element has no relations
        if i==0 or i==len(relation)-1:
            continue
        candidate=relation[j]
        ith_link=[candidate[0]]#closest in time with a relation is always a link
        for index,value in enumerate(candidate[1:]):
            append=0
            for k in candidate[0:index+1]:
                if k<j and value in link[k]:
                    append+=1
                    break
                elif k>=j and value in relation[k]:
                    append+=1
                    break
            if append==0:
                ith_link.append(value)
        link[j]=ith_link
    return link

def longest_chain(link):
    maximal=[]
    for i in link[0]:
        maximal.append([0,i])
    flow=1
    while flow>0:
        flow=0
        maximal_copy=[]
        for i in maximal:
            if i=='remove':
                continue
            if link.get(i[-1])==None:
                continue
            for j in link[i[-1]]:
                for k in maximal:#check for longer route by removing shorter routes to the same point
                    if j in k and not j==k[-1]:
                        k='remove'
                element=i.copy()
                element.append(j)
                maximal_copy.append(element)
                flow+=1
        if flow!=0:
            maximal=maximal_copy
    return maximal
            



if __name__=='__main__':
    import ADS2 as ads
    N=50
    flat=ads.sprinkle(2,N,2)

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
    lonk=link(relation)
    print(lonk)
    long=longest_chain(lonk)
    print("longest chains:",long)
    print([len(i) for i in long])