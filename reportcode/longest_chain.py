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