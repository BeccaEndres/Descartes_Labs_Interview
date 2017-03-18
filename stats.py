#Do tasks 1 & 2 in the comments in img_stats/stats.py
#The answer to task 1 should match max_cut180.tif

# Task 1:
# clouds make the max image almost all white
# make a max image where values in the img[] array larger than 180 don't count
# you can do this with your choice of numpy or Cython/C

#!/usr/bin/env python
import sys
import numpy as np
from osgeo import gdal
# import img_stats
# Usage: ./stats.py *.jp2
import img_stats
from _img_stats import cmin

opts = ["COMPRESS=LZW"]
driver = gdal.GetDriverByName('GTiff')
obj = gdal.Open(sys.argv[1], gdal.gdalconst.GA_ReadOnly)
rows = obj.RasterYSize
cols = obj.RasterXSize
img = np.zeros((3,rows,cols,len(sys.argv[1:])), dtype=np.uint8)
for i,arg in enumerate(sys.argv[1:]):
    print "Reading %s" % arg
    obj = gdal.Open(arg, gdal.gdalconst.GA_ReadOnly)
    _x = obj.ReadAsArray()
    _x = np.clip(0.1 * _x, 0, 255) 
    img[:,:,:,i] =  _x.astype('uint8')

# max image value to send to cmin then not count values greater than 180
imgmax = np.zeros(img.shape[0:3], dtype = 'uint8') 

# min image value to send to cim then ignore values where there is no data
imgmin = np.zeros(img.shape[0:3], dtype = 'uint8') 
img_stats.cmin(img, imgmin, imgmax)

# output file of task 1
outds_max = driver.Create("max.tif", cols, rows, 3, gdal.GDT_Byte, options=opts)

# output file of tast 2
outds_min = driver.Create("min.tif", cols, rows, 3, gdal.GDT_Byte, options=opts)

for b in range(3):
    outds_max.GetRasterBand(b+1).WriteArray(imgmax[b])
    outds_min.GetRasterBand(b+1).WriteArray(imgmax[b])
del outds


