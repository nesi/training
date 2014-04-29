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
#from numba import jit

curPath = os.path.abspath(os.path.curdir)
inputDir = os.path.join(curPath,'noisy')
outputDir = os.path.join(curPath,'denoised')

#@jit
def loop(imgFiles):
	for f in imgFiles:
		img = img_as_float(data.load(os.path.join(inputDir,f)))
		startTime = time.time()
		img = filter.denoise_bilateral(img, sigma_range=0.2, sigma_spatial=10),
		io.imsave(os.path.join(outputDir,f), img)
		print("Took {} seconds for {}".format(time.time() - startTime, f))

def serial():
	total_start_time = time.time()
	imgFiles=["%.4d.jpg"%x for x in range(1,101)]
	loop(imgFiles)
	print("Total time {} seconds".format(time.time() - total_start_time))

if __name__=='__main__':
	serial()

	



