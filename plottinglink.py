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