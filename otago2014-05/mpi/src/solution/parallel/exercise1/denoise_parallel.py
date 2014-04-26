"""
=============================
Denoising the picture of Lena
=============================

In this example, we denoise a noisy version of the picture of Lena using the
total variation and bilateral denoising filter.

These algorithms typically produce "posterized" images with flat domains
separated by sharp edges. It is possible to change the degree of posterization
by controlling the tradeoff between denoising and faithfulness to the original
image.

Total variation filter
----------------------

The result of this filter is an image that has a minimal total variation norm,
while being as close to the initial image as possible. The total variation is
the L1 norm of the gradient of the image.

Bilateral filter
----------------

A bilateral filter is an edge-preserving and noise reducing filter. It averages
pixels based on their spatial closeness and radiometric similarity.

"""
import numpy as np

from skimage import data, img_as_float
from skimage.filter import denoise_tv_chambolle, denoise_bilateral,denoise_tv_bregman
import skimage.io

import os.path
import time
from mpi4py import MPI
from numba import jit

curPath = os.path.abspath(os.path.curdir)

noisyDir = os.path.join(curPath,'noisy')
denoisedDir = os.path.join(curPath,'denoised')

@jit
def loop(imgFiles,rank):
	for f in imgFiles:
		img = img_as_float(data.load(os.path.join(noisyDir,f)))
		startTime = time.time()
	#	img = denoise_tv_chambolle(img, weight=0.08, multichannel=True),
		img = denoise_bilateral(img, sigma_range=0.1, sigma_spatial=3),
		skimage.io.imsave(os.path.join(denoisedDir,f), img)
		print("Process %d: Took %f seconds for %s" %(rank, time.time() - startTime, f))

def parallel():

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size() #size must be 4!!
	
	totalStartTime = time.time()
	
	
	imgFiles = os.listdir(noisyDir)
	imgFiles=[x for x in imgFiles if '.jpg' in x]
	imgFiles.sort()

	numFiles = len(imgFiles)/size #number of files this process will handle
	imgFiles = imgFiles[rank*numFiles:(rank+1)*numFiles] #list of files this process will handle
	loop(imgFiles,rank)
	
	print("Process %d: Total time %f seconds" %(rank, time.time() - totalStartTime))

if __name__=='__main__':
	parallel()

	



