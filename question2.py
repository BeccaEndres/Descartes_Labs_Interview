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
	
	# retrieves all bands from image
	d = o.ReadAsArray()

	i = 0
	while i < 9:	
		band = o.GetRasterBand(i)
		print band
		i = i + 1
	
	block_sizes = band.GetBlockSize()
	x_block_size = block_sizes[0]
	y_block_size = block_sizes[1]

	xsize = band.XSize
	ysize = band.YSize

	print x_block_size
	print y_block_size
	print xsize
	print ysize

	print d.shape	

	cov_matrix = []
#	for i in d:
#		print d[i]
#		cov_matrix = np.cov(d[i])
	

#	plt.plot(d)
#	plt.axis('')
#	plt.show()

if __name__ == "__main__":
	main()


