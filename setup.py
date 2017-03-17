from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
# python setup.py build_ext --inplace
import numpy
setup (
	cmdclass = {'build_ext':build_ext},
	ext_modules=[Extension("img_stats",
	sources=["_img_stats.pyx","cmin.c"],
	include_dirs=[numpy.get_include()],
	extra_compile_args=["-std=c99"],)]
)

