#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>
#include <pythread.h>
#include <math.h>

#define Error(args...) do { fprintf(stderr, args);exit(1); } while(0)

#define idx4(i, j, k, l, ii, jj, kk, ll)(ptrdiff_t)(i)*(jj)*(kk)*(ll)+(ptrdiff_t)(j)*(kk)*(ll)+(ptrdiff_t)(k)*(ll)+(l)

#define idx3(i, j, k, ii, jj, kk)(i)*(jj)*(kk)+(j)*(kk)+(k)

#define idx2(j, k, jj, kk)(j)*(kk)+(k)

static void _cmin(unsigned char *img, const int ii, const int jj, const int kk, const int ll, unsigned char *out)
{
	print "checkpoint 1"
}
