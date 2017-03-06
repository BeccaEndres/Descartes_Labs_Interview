# Using any image available in the dgsamples pypi package:
#
# 1. retrieve all bands from the image
# 2. compute the covariance matrix of the image bands
# 3. plot the covariance matrix and save the figure to disk in
#    png format
# You may use the initial few lines of code below if you like
#import dgsamples
#from osgeo import gdal
#import numpy as np
#import matplotlib.pyplot as plt
#o = gdal.Open(dgsamples.bayou_chip.extract_test)
#d = o.ReadAsArray()


import dgsamples
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

def main():
	o = gdal.Open(dgsamples.bayou_chip.extract_test)
	d = o.ReadAsArray()


if __name__ == "__main__":
	main()


