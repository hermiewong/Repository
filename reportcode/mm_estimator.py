from scipy.special import gamma
import scipy.optimize as so

def ordering_frac(d):
    return (gamma(d+1) * gamma(d/2)) / (4 * gamma(3/2 * d))

def root_func(d, f):
    return ordering_frac(d) - f

def mm_dimension(f):
    """
    f:ordering fraction
    """
    sol=so.root(root_func,1,(f))
    d=sol["x"]
    return d[0]