import matplotlib.pyplot as plt

def plot(position_subset,array_of_chain,xindex,yindex,scatter=True,show=False):
    """
    position_subset must be in time order
    array_of_chain is an array of different chains represented by a list of indices
    xindex: position of x index within position_subset to be plotted
    yindex: position of y index within position_subset to be plotted
    """
    if scatter==True:
        plt.scatter(position_subset[:,xindex],position_subset[:,yindex])
    for i in range(len(array_of_chain)-1):
        plt.plot([position_subset[array_of_chain[i],xindex],position_subset[array_of_chain[i+1],xindex]],[position_subset[array_of_chain[i],yindex],position_subset[array_of_chain[i+1],yindex]])
    if show==True:
        plt.show()

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


if __name__=='__main__':
    from ADS2 import sprinkle
    import matplotlib.pyplot as plt
    flat=sprinkle(1,10,2)

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
    lonk=link(relation)
    plt.rcParams.update({'axes.labelsize':14,'xtick.labelsize':12,'ytick.labelsize':12})
    for i in range(len(flat)):
        plt.plot(flat[i,0],flat[i,1])
        plt.text(flat[i,0],flat[i,1],i,size=14)
    for i in lonk:
        for j in lonk[i]:
            plt.plot([flat[i,0],flat[j,0]],[flat[i,1],flat[j,1]],color='b')
    
    plt.xlabel('x')
    plt.ylabel('t')
    plt.grid()
    plt.show()
