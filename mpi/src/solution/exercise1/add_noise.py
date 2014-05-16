from scipy.misc import imread,imsave
import numpy as np
import os.path
import time

curpath = os.path.abspath(os.path.curdir)

noisy_dir = os.path.join(curpath,'noisy')

original_dir=os.path.join(curpath,'original')
imgfiles = os.listdir(original_dir)
imgfiles=[x for x in imgfiles if '.jpg' in x]
imgfiles.sort()

total_start_time = time.time()

for f in imgfiles:
	print "Processing %s" %f
	start_time = time.time()
	img = imread(os.path.join(original_dir,f)).astype(np.float32)
	random_data=np.random.randn(img.shape[0],img.shape[1])
	noisy_img=img+8.*random_data
	imsave(os.path.join(noisy_dir,f),noisy_img)
	print "Took %f seconds" %(time.time() - start_time)

