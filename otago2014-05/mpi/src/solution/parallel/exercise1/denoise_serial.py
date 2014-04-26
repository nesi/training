"""
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
from skimage.filter import denoise_bilateral
import skimage.io

import os.path
import time

from numba import jit

curPath = os.path.abspath(os.path.curdir)
noisyDir = os.path.join(curPath,'noisy')
denoisedDir = os.path.join(curPath,'denoised')

@jit
def loop(imgFiles):
	for f in imgFiles:
		img = img_as_float(data.load(os.path.join(noisyDir,f)))
		startTime = time.time()
	#	img = denoise_tv_chambolle(img, weight=0.08, multichannel=True),
		img = denoise_bilateral(img, sigma_range=0.2, sigma_spatial=10),
		skimage.io.imsave(os.path.join(denoisedDir,f), img)
		print("Took {} seconds for {}".format(time.time() - startTime, f))


def serial():
	total_start_time = time.time()
	imgFiles = os.listdir(noisyDir)
	imgFiles=[x for x in imgFiles if '.jpg' in x]
	imgFiles.sort()
	loop(imgFiles)
	print("Total time {} seconds".format(time.time() - total_start_time))

if __name__=='__main__':
	serial()

	



