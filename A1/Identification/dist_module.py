import numpy as np
import math



# Compute the intersection distance between histograms x and y
# Return 1 - hist_intersection, so smaller values correspond to more similar histograms
# Check that the distance range in [0,1]

def dist_intersect(x,y):
    sum1 = np.sum(x)
    sum2 = np.sum(y)
    
    array_min = [min(x[i], y[i]) for i in range(len(x))]

    return 1 - (1/2*((np.sum(array_min)/sum1)+((np.sum(array_min)/sum2))))




# Compute the L2 distance between x and y histograms
# Check that the distance range in [0,sqrt(2)]
l2 = lambda x,y: (x-y)**2

def dist_l2(x,y):
    c = 0
    for i in range(len(x)):
        c += l2(x[i], y[i])
    return c



# Compute chi2 distance between x and y
# Check that the distance range in [0,Inf]
# Add a minimum score to each cell of the histograms (e.g. 1) to avoid division by 0

def dist_chi2(x,y):
    c = 0
    for i in range(len(x)):
        if x[i] <= 0:
            x[i] = 1
        if y[i] <= 0:
            y[i] = 1
        c += l2(x[i], y[i])/(x[i] + y[i])

    return c



def get_dist_by_name(x, y, dist_name):
    if dist_name == 'chi2':
        return dist_chi2(x,y)
    elif dist_name == 'intersect':
        return dist_intersect(x,y)
    elif dist_name == 'l2':
        return dist_l2(x,y)
    else:
        assert False, 'unknown distance: %s'%dist_name





