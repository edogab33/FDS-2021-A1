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
    up = int(3*sigma)
    x = list()
    Gx = list()
    for i in range(lb, up+1):
        x.append(i)
        Gx.append((1 / math.sqrt(2 * math.pi * sigma)) * math.exp(-i ** 2 / (2 * sigma ** 2)))

    return Gx, x


"""
Implement a 2D Gaussian filter, leveraging the previous gauss.
Implement the filter from scratch or leverage the convolve2D method (scipy.signal)
Leverage the separability of Gaussian filtering
Input: image, sigma (standard deviation)
Output: smoothed image
"""

def GaussianMatrix(X,sigma):
       row,col=X.shape
       GassMatrix=np.zeros(shape=(row,row))
       X=np.asarray(X)
       i=0
       for v_i in X:
           j=0
           for v_j in X:
               GassMatrix[i,j]=Gaussian(v_i.T,v_j.T,sigma)
               j+=1
           i+=1
       return GassMatrix

def Gaussian(x,z,sigma):
       return np.exp((-(np.linalg.norm(x-z)**2))/(2*sigma**2))


def gaussianfilter(img, sigma):
    img = np.array(img)
    kernel = GaussianMatrix(img, sigma)
    conv2(img, kernel)
    return smooth_img


"""
Gaussian derivative function taking as argument the standard deviation sigma
The filter should be defined for all integer values x in the range [-3sigma,3sigma]
The function should return the Gaussian derivative values Dx computed at the indexes x
"""


def gaussdx(sigma):

    # ...

    return Dx, x


def gaussderiv(img, sigma):

    # ...

    return imgDx, imgDy
