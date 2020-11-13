import numpy as np
import matplotlib.pyplot as plt

import histogram_module
import dist_module
import match_module



# compute and plot the recall/precision curve
#
# D - square matrix, D(i, j) = distance between model image i, and query image j
#
# note: assume that query and model images are in the same order, i.e. correct answer for i-th query image is the i-th model image

def plot_rpc(D, plot_color):
    
    recall = []
    precision = []
    num_queries = D.shape[1]
    
    num_images = D.shape[0]
    assert(num_images == num_queries), 'Distance matrix should be a square matrix'
    
    labels = np.diag([1]*num_images)
      
    d = D.reshape(D.size)
    l = labels.reshape(labels.size)
     
<<<<<<< HEAD
    sortidx = d.argsort() #list of indexes
    d = d[sortidx] #sorted according to sortidx
    l = l[sortidx] #those with l = 1 are tp, if the distance is < threshold it means that are false negative

    max_val = np.amax(d)
    min_val = np.min(d)

    incr = (max_val - min_val) / 100000
=======
    sortidx = d.argsort()
    d = d[sortidx]
    l = l[sortidx]
    
    tp = 0
    #... (your code here)
    
        incr = (max_val - min_val) / 10000
>>>>>>> 345bd372a7ea5720e50e877d5931ffd8c758623a

    for t in np.arange(min_val, max_val+incr, incr):
        tp = 0
        tn = 0
        fn = 0
        fp = 0
        for i in range(len(d)):
            if d[i] <= t:
                if l[i] == 1:
                    tp += 1
                else:
                    fp += 1
            else:
                if l[i] == 0:
                    tn += 1
                else:
                    fn += 1
        #Compute precision and recall values and append them to "recall" and "precision" vectors
        #... (your code here)
        precision.append(tp/(tp+fp))
        recall.append(tp/(tp+fn))
<<<<<<< HEAD

=======
    
>>>>>>> 345bd372a7ea5720e50e877d5931ffd8c758623a
    plt.plot([1-precision[i] for i in range(len(precision))], recall, plot_color+'-')


def compare_dist_rpc(model_images, query_images, dist_types, hist_type, num_bins, plot_colors):
    
    assert len(plot_colors) == len(dist_types), 'number of distance types should match the requested plot colors'

    for idx in range( len(dist_types) ):

        [best_match, D] = match_module.find_best_match(model_images, query_images, dist_types[idx], hist_type, num_bins)

        plot_rpc(D, plot_colors[idx])
    

    plt.axis([0, 1, 0, 1]);
    plt.xlabel('1 - precision');
    plt.ylabel('recall');
    
    # legend(dist_types, 'Location', 'Best')
    
    plt.legend( dist_types, loc='best')


# TO DELETE
with open('/Users/edoardogabrielli/Documents/Università/ComputerScience/FoundationsOfDataScience/fds-2021/A1/Identification/model.txt') as fp:
    model_images = fp.readlines()
model_images = [x.strip() for x in model_images] 

with open('/Users/edoardogabrielli/Documents/Università/ComputerScience/FoundationsOfDataScience/fds-2021/A1/Identification/query.txt') as fp:
    query_images = fp.readlines()
query_images = [x.strip() for x in query_images] 

num_bins = 20;


plt.figure(8)
compare_dist_rpc(model_images, query_images, ['chi2', 'intersect', 'l2'], 'rg', num_bins, ['r', 'g', 'b'])
plt.title('RG histograms')
plt.show()


