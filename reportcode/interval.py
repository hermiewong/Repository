import numpy as np
def filter_interval(position,l,interval_centre):
    # position - the numpy array with all the points. Needs to be sorted by the
    #          time coordinate.
    # l is the height of the double cone, end to end.
    # interval centre - yet again, numpy array with the interval centre.
    # Expected coordinate order: R, t, x_i,
    position_subset=[]
    t_c=interval_centre[1]
    for i in position:
        pi=i
        ti=i[1]
        diff = pi-interval_centre
        delta_t=np.abs(diff[1])
        if delta_t <=0.5*l:
            r_max = l/2 - delta_t
            r_max_squared = r_max**2
            r_squared = diff[0]**2 + sum(diff[2:]**2)
            if r_squared <= r_max_squared:
                position_subset.append(i)
        elif ti> t_c:
            break
    position_subset=np.array(position_subset)
    return position_subset