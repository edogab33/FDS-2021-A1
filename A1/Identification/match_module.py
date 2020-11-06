import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

import histogram_module
import dist_module

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray



# model_images - list of file names of model images
# query_images - list of file names of query images
#
# dist_type - string which specifies distance type:  'chi2', 'l2', 'intersect'
# hist_type - string which specifies histogram type:  'grayvalue', 'dxdy', 'rgb', 'rg'
#
# note: use functions 'get_dist_by_name', 'get_hist_by_name' and 'is_grayvalue_hist' to obtain 
#       handles to distance and histogram functions, and to find out whether histogram function 
#       expects grayvalue or color image

def find_best_match(model_images, query_images, dist_type, hist_type, num_bins):

    hist_isgray = histogram_module.is_grayvalue_hist(hist_type)
    
    model_hists = compute_histograms(model_images, hist_type, hist_isgray, num_bins)
    query_hists = compute_histograms(query_images, hist_type, hist_isgray, num_bins)
    
    D = np.zeros((len(model_images), len(query_images)))

    best_match = np.zeros(len(query_images))

    for i in range(len(model_hists)):
        for j in range(len(query_hists)):
            D[i, j] = dist_module.get_dist_by_name(query_hists[j], model_hists[i], dist_type)

    for i in range(len(best_match)):
        best_match[i] = np.where(D == np.amin(D[:,i]))[0][0]

    return best_match, D



def compute_histograms(image_list, hist_type, hist_isgray, num_bins):
    
    image_hist = []

    # Compute hisgoram for each image and add it at the bottom of image_hist

    for i in image_list:
        img = np.array(Image.open(os.path.join(THIS_FOLDER, i)), float)
        if hist_isgray:
            img = rgb2gray(img)
        image_hist.append(histogram_module.get_hist_by_name(img, num_bins, hist_type))

    return image_hist



# For each image file from 'query_images' find and visualize the 5 nearest images from 'model_image'.
#
# Note: use the previously implemented function 'find_best_match'
# Note: use subplot command to show all the images in the same Python figure, one row per query image

def show_neighbors(model_images, query_images, dist_type, hist_type, num_bins):
    
    
    plt.figure()
    plt.title("Top 5 neighbors")

    num_nearest = 5  # show the top-5 neighbors
    
    best_match, D = find_best_match(model_images, query_images, dist_type, hist_type, num_bins)

    fig, ax = plt.subplots(len(query_images), 6)
    pos = 1
    for i in range(len(query_images)):

        img = np.array(Image.open(os.path.join(THIS_FOLDER, query_images[i])))
        pos = 6*i + 1
        plt.subplot(len(query_images), 6, pos)
        plt.imshow(img)

        for j in range(1,6):
            best_match = np.amin(D[:,i])

            model_index = np.where(D == best_match)[0][0]
            D[model_index][i] = 10

            img = np.array(Image.open(os.path.join(THIS_FOLDER, model_images[model_index])))

            plt.subplot(len(query_images), 6, pos+j)
            plt.imshow(img)

    plt.show()


