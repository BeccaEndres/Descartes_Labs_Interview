import numpy as np
cimport numpy as np
cimport cython
cdef extern from "stdlib.h":
    ctypedef void const_void "const void"
cdef extern from "img_stats.h":
    void _cmin(unsigned char *img, int ii, int jj, int kk, int ll,
               unsigned char *out) nogil
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef cmin(unsigned char[:,:,:,::1] arr, unsigned char[:,:,:,::1] out):
    _cmin(&arr[0,0,0,0], arr.shape[0], arr.shape[1], arr.shape[2],
          arr.shape[3], &out[0,0,0,0])
    return None
