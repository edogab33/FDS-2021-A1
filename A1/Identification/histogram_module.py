import numpy as np
from numpy import histogram as hist
from copy import deepcopy
import sys
import gauss_module as gm # NOTE: Import gauss_module from Filtering doesn't work, so I copied the file in this folder


#Add the Filtering folder, to import the gauss_module.py file, where gaussderiv is defined (needed for dxdy_hist)
import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
filteringpath = os.path.join(parentdir, 'Filtering')
sys.path.insert(0,filteringpath)
import gauss_module



#  compute histogram of image intensities, histogram should be normalized so that sum of all values equals 1
#  assume that image intensity varies between 0 and 255
#
#  img_gray - input image in grayscale format
#  num_bins - number of bins in the histogram
def normalized_hist(img_gray, num_bins):
  assert len(img_gray.shape) == 2, 'image dimension mismatch'
  assert img_gray.dtype == 'float', 'incorrect image type'
  data = []
  for row in img_gray:
    for col in row:
      data.append(col)
  data = np.array(data)
  
  bin_array = np.linspace(0,255,num_bins)
  
  my_histogram = []
  for i in range(len(bin_array)-1):
    # Each True value in mask represents the pixel of given intensity which should be in the bin bin_array[i].
    mask = (data >= bin_array[i]) & (data < bin_array[i+1])
    my_histogram.append(len(data[mask])) # Count every pixel which should be in the bin with True value in mask.

  my_histogram /= np.sum(my_histogram)
  return my_histogram, bin_array

#  Compute the *joint* histogram for each color channel in the image
#  The histogram should be normalized so that sum of all values equals 1
#  Assume that values in each channel vary between 0 and 255
#
#  img_color - input color image
#  num_bins - number of bins used to discretize each channel, total number of bins in the histogram should be num_bins^3
#
#  E.g. hists[0,9,5] contains the number of image_color pixels such that:
#       - their R values fall in bin 0
#       - their G values fall in bin 9
#       - their B values fall in bin 5
def rgb_hist(img_color_double, num_bins):
    assert len(img_color_double.shape) == 3, 'image dimension mismatch'
    assert img_color_double.dtype == 'float', 'incorrect image type'

    #Define a 3D histogram  with "num_bins^3" number of entries
    hists = np.zeros((num_bins, num_bins, num_bins))

    bin_array = np.linspace(0,255,num_bins)

    img = np.reshape(img_color_double, (len(img_color_double[0])*len(img_color_double), 3))

    #Loop for each pixel i in the image
    for i in range(img_color_double.shape[0]*img_color_double.shape[1]):
        # Increment the histogram bin which corresponds to the R,G,B value of the pixel i

        # Take R, G and B
        r = img[i][0]
        g = img[i][1]
        b = img[i][2]

        # Calculate R, G and B indexes
        i_r = 0
        i_g = 0
        i_b = 0

        for j in range(len(bin_array)-1):
          if ((r >= bin_array[j]) & (r < bin_array[j+1])):
            i_r = np.where(bin_array == bin_array[j])[0][0]
          elif ((g >= bin_array[j]) & (g < bin_array[j+1])):
            i_g = np.where(bin_array == bin_array[j])[0][0]
          elif ((b >= bin_array[j]) & (b < bin_array[j+1])):
            i_b = np.where(bin_array == bin_array[j])[0][0]

        hists[i_r][i_g][i_b] += 1


    #Normalize the histogram such that its integral (sum) is equal 1
    hists /= np.sum(hists)

    #Return the histogram as a 1D vector
    hists = hists.reshape(hists.size)
    return hists



#  Compute the *joint* histogram for the R and G color channels in the image
#  The histogram should be normalized so that sum of all values equals 1
#  Assume that values in each channel vary between 0 and 255
#
#  img_color - input color image
#  num_bins - number of bins used to discretize each channel, total number of bins in the histogram should be num_bins^2
#
#  E.g. hists[0,9] contains the number of image_color pixels such that:
#       - their R values fall in bin 0
#       - their G values fall in bin 9
def rg_hist(img_color_double, num_bins):
    assert len(img_color_double.shape) == 3, 'image dimension mismatch'
    assert img_color_double.dtype == 'float', 'incorrect image type'

    #Define a 2D histogram  with "num_bins^2" number of entries
    hists = np.zeros((num_bins, num_bins))

    bin_array = np.linspace(0,255,num_bins)

    img = np.reshape(img_color_double, (len(img_color_double[0])*len(img_color_double), 3))

    #Loop for each pixel i in the image
    for i in range(img_color_double.shape[0]*img_color_double.shape[1]):
        # Increment the histogram bin which corresponds to the R,G,B value of the pixel i

        # Take R, G
        r = img[i][0]
        g = img[i][1]

        # Calculate R, G
        i_r = 0
        i_g = 0

        for j in range(len(bin_array)-1):
          if ((r >= bin_array[j]) & (r < bin_array[j+1])):
            i_r = np.where(bin_array == bin_array[j])[0][0]
          elif ((g >= bin_array[j]) & (g < bin_array[j+1])):
            i_g = np.where(bin_array == bin_array[j])[0][0]

        hists[i_r][i_g] += 1

    #Normalize the histogram such that its integral (sum) is equal 1
    hists /= np.sum(hists)

    #Return the histogram as a 1D vector
    hists = hists.reshape(hists.size)

    return hists




#  Compute the *joint* histogram of Gaussian partial derivatives of the image in x and y direction
#  Set sigma to 3.0 and cap the range of derivative values is in the range [-6, 6]
#  The histogram should be normalized so that sum of all values equals 1
#
#  img_gray - input gray value image
#  num_bins - number of bins used to discretize each dimension, total number of bins in the histogram should be num_bins^2
#  hists[30, 10] means:
#  - img_dx pixel intensity falls in bin 30
#  - img_dy pixel intensity falls in bin 10
#  Note: you may use the function gaussderiv from the Filtering exercise (gauss_module.py)
def dxdy_hist(img_gray, num_bins):
    assert len(img_gray.shape) == 2, 'image dimension mismatch'
    assert img_gray.dtype == 'float', 'incorrect image type'


    sigma = 3.0
    img_dx, img_dy = gm.gaussderiv(img_gray, sigma)

    imgx = np.reshape(img_dx, (len(img_dx[0])*len(img_dx)))
    imgy = np.reshape(img_dy, (len(img_dy[0])*len(img_dy)))

    #Define a 2D histogram  with "num_bins^2" number of entries
    hists = np.zeros((num_bins, num_bins))

    bin_array = np.linspace(0,255,num_bins)

    for i in range(len(imgx)):
        in_x = imgx[i]
        in_y = imgy[i]

        # Calculate R, G
        i_x = 0
        i_y = 0

        for j in range(len(bin_array)-1):
          if ((in_x >= bin_array[j]) & (in_x < bin_array[j+1])):
            i_x = np.where(bin_array == bin_array[j])[0][0]
          elif ((in_y >= bin_array[j]) & (in_y < bin_array[j+1])):
            i_y = np.where(bin_array == bin_array[j])[0][0]

        hists[i_x][i_y] += 1



    #Normalize the histogram such that its integral (sum) is equal 1
    hists /= np.sum(hists)

    #Return the histogram as a 1D vector
    hists = hists.reshape(hists.size)
    return hists



def is_grayvalue_hist(hist_name):
  if hist_name == 'grayvalue' or hist_name == 'dxdy':
    return True
  elif hist_name == 'rgb' or hist_name == 'rg':
    return False
  else:
    assert False, 'unknown histogram type'


def get_hist_by_name(img, num_bins_gray, hist_name):
  if hist_name == 'grayvalue':
    return normalized_hist(img, num_bins_gray)
  elif hist_name == 'rgb':
    return rgb_hist(img, num_bins_gray)
  elif hist_name == 'rg':
    return rg_hist(img, num_bins_gray)
  elif hist_name == 'dxdy':
    return dxdy_hist(img, num_bins_gray)
  else:
    assert False, 'unknown distance: %s'%hist_name

