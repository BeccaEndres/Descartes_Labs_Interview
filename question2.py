# Using any image available in the dgsamples pypi package:
#
# 1. retrieve all bands from the image
# 2. compute the covariance matrix of the image bands
# 3. plot the covariance matrix and save the figure to disk in
#    png format

import dgsamples
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

def main():
	o = gdal.Open(dgsamples.bayou_chip.extract_test)
	
	# retrieves all bands from image into 3D array
	d = o.ReadAsArray()

	i = 1
	Cov = []

	# Gets one band at a time and computes it's covariance
	while i < 9:	
		band = o.GetRasterBand(i)	
		Cov = np.cov(band.ReadAsArray())
		i += 1
		
	
if __name__ == "__main__":
	main()


