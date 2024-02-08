def link(relation):
    link={}
    #for bottom point we know top point will not be link so
    #we bypass this point with a separate loop
    candidate=relation[0]
    ith_link=[candidate[0]]#closest in time with a relation is always a link
    for index,value in enumerate(candidate[1:-1]):
        for k in candidate[0:index+1]:#don't need to check the current candidate and any future candidates
            if value in relation[k]:
                break
            else: ith_link.append(value)
    link[0]=ith_link

    for i in relation[1:-1]:#last element has no relations
        candidate=relation[i]
        ith_link=[candidate[0]]#closest in time with a relation is always a link
        for index,value in enumerate(candidate[1:]):
            for k in candidate[0:index+1]:
                if k<i and value in link[k]:
                    break
                elif k>=i and value in relation[k]:
                    break
                else:
                    ith_link.append(value)
        link[i]=ith_link
    return link

def maximal_chain(relation):
    #relations are sorted in time order
    maximal={}
