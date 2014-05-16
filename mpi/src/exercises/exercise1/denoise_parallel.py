"""
Bilateral filter
----------------

A bilateral filter is an edge-preserving and noise reducing filter. It averages
pixels based on their spatial closeness and radiometric similarity.

"""
import numpy as np
from skimage import data, img_as_float, filter, io
import os.path
import time
from mpi4py import MPI

curPath = os.path.abspath(os.path.curdir)
inputDir = os.path.join(curPath,'noisy')
outputDirg = os.path.join(curPath,'denoised')

def loop(imgFiles):
	for f in imgFiles:
		img = img_as_float(data.load(os.path.join(inputDir,f)))
		startTime = time.time()
		img = filter.denoise_bilateral(img, sigma_range=0.1, sigma_spatial=3)
		io.imsave(os.path.join(outputDirg,f), img)
		print("Took %f seconds for %s" %(time.time() - startTime, f))

def parallel():
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size() #size must be a factor of 100
	totalStartTime = time.time()
	
	numFiles = 100/size #number of files this process will handle
	imgFiles = ["%.4d.jpg"%x for x in range(???:???)] # Fix this line to distribute imgFiles
	loop(imgFiles)
	print("Process %d: Total time %f seconds" %(rank, time.time() - totalStartTime))

if __name__=='__main__':
	parallel()

	



