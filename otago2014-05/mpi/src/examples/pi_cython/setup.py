from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("pi_cython", ["pi_cython.pyx"])]

setup(
	name = 'Cython Pi approximation app',
	cmdclass={'build_ext':build_ext},
	ext_modules = ext_modules
)

