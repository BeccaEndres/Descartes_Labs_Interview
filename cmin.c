// Task 2:
// make a min image where NODATA (values == 0) are ignored
// Implement this in C using the provided Cython shim and template in cmin.c

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
_cmin(unsigned char *img, const int ii, const int jj, const int kk, const int ll, unsigned char *out)
{
	printf("ch1");


}
