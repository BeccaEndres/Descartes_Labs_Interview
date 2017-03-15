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
    _x = np.clip(_x, 0, 180) # clips values greater than 180 and sets them to 180
    img[:,:,:,i] =  _x.astype('uint8')
imgmax = np.amax(img, axis=3)
outds  = driver.Create("max.tif", cols, rows, 3, gdal.GDT_Byte, options=opts)
for b in range(3):
    outds.GetRasterBand(b+1).WriteArray(imgmax[b])
del outds

# Task 2:
# make a min image where NODATA (values == 0) are ignored
# Implement this in C using the provided Cython shim and template in cmin.c

#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include "img_stats.h"
#define Error(args...) \
    do { \
       fprintf(stderr, args); \
       exit(1); \
    } while(0)
#define idx4(i, j, k, l, ii, jj, kk, ll) \
    (ptrdiff_t)(i)*(jj)*(kk)*(ll)+(ptrdiff_t)(j)*(kk)*(ll)+(ptrdiff_t)(k)*(ll)+(l)
#define idx3(i, j, k, ii, jj, kk) \
    (i)*(jj)*(kk)+(j)*(kk)+(k)
#define idx2(j, k, jj, kk) \
    (j)*(kk)+(k)
void
_cmin(unsigned char *img, const int ii, const int jj, const int kk, const int ll,
      unsigned char *out)
{


}
