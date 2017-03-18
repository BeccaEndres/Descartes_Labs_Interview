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
	d = o.ReadAsArray()

	means = [np.mean(ros) for ros in d]
	cov = np.zeros((d.shape[0], d.shape[0]))	

	# formula for coputing the covariance matris of the bands
	for i in range(d.shape[0]):
		for j in range(i + 1):
			cov[j][i] = cov[i][j] = np.sum(np.multiply(d[i] - means[i],d[j] - means[j]))/(d[i].size - 1)
		

	plt.plot(cov) 
        plt.savefig('Covariance.png') #saves plot in png format


if __name__ == "__main__":
	main()


