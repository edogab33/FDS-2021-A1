# import packages: numpy, math (you might need pi for gaussian functions)
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import convolve2d as conv2


"""
Gaussian function taking as argument the standard deviation sigma
The filter should be defined for all integer values x in the range [-3sigma,3sigma]
The function should return the Gaussian values Gx computed at the indexes x
"""


def gauss(sigma):
    lb = int(-3*sigma)
    ub = int(3*sigma)
    x = list()
    Gx = list()
    for i in range(lb, ub+1):
        x.append(i)
        Gx.append((1 / math.sqrt(2 * math.pi) * sigma) * math.exp(-i ** 2 / (2 * sigma ** 2)))
    return Gx, x


"""
Implement a 2D Gaussian filter, leveraging the previous gauss.
Implement the filter from scratch or leverage the convolve2D method (scipy.signal)
Leverage the separability of Gaussian filtering
Input: image, sigma (standard deviation)
Output: smoothed image
"""

def gaussianfilter(img, sigma):
    img = np.array(img)
    gx, x = gauss(sigma)

    filter_kernel = np.outer(gx, gx) # outer product, to obtain a matrix
    filter_kernel /= np.sum(filter_kernel)  # normalize the matrix

    smooth_img = conv2(img, filter_kernel, mode="same") # 'mode="same"' eliminates black padding
    return smooth_img


"""
Gaussian derivative function taking as argument the standard deviation sigma
The filter should be defined for all integer values x in the range [-3sigma,3sigma]
The function should return the Gaussian derivative values Dx computed at the indexes x
"""


def gaussdx(sigma):
    lb = int(-3*sigma)
    ub = int(3*sigma)
    x = list()
    Dx = list()

    for i in range(lb, ub+1):
        x.append(i)
        Dx.append(-(i / math.sqrt(2 * math.pi) * sigma**3) * math.exp(-i ** 2 / (2 * sigma ** 2)))

    return Dx, x


def gaussderiv(img, sigma):

    # ...

    return imgDx, imgDy
