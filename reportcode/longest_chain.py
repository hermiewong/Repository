def find_relation(position):
    relation={}
    for i,base in enumerate(position):
        ith=[]
        for j,check in enumerate(position[i+1:]):
            vector=check-base
            tausq=vector[1]**2-vector[0]**2-sum(vector[2:]**2)
            if tausq>0:
                ith.append(j+i+1)
        relation[i]=ith
    return relation

def find_link(position):
    link={}
    for i,base in enumerate(position):
        ith=[]
        for j,check in enumerate(position[i+1:]):
            notlink=0
            for k in ith:
                vector=check-position[k]
                tausq=vector[1]**2-vector[0]**2-sum(vector[2:]**2)
                if tausq>0:
                    notlink+=1
                    break
            if notlink==1:
                continue
            vector=check-base
            tausq=vector[1]**2-vector[0]**2-sum(vector[2:]**2)
            if tausq>0:
                ith.append(j+i+1)
        link[i]=ith
    return link

def longest_chain(link):
    """
    link: dictionary of links
    """
    maximal=[]
    for i in link[0]:
        maximal.append([0,i])
    flow=1
    while flow>0:
        flow=0
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
    return maximal[0]