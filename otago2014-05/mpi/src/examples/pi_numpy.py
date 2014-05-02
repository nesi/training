# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:21:24 2013

@author: Sung Bae
"""
import time
from numpy import *

def Pi():
	num_steps = 100000000

	sum = 0
	start = time.time()
	step = 1.0/num_steps
	# Do something here to replace the for loop (3 lines)
	# for i in xrange(num_steps):
	#  x=(i+0.5)*step
	#  sum = sum + 4.0/(1.0+x*x)
	i=arange(num_steps)
	x=(i+0.5)*step
	sum = (4.0/(1.0+x*x)).sum()

	pi = step * sum

	end = time.time()
	print "Pi with %d steps is %.20f in %f secs" %(num_steps, pi, end-start)

if __name__ == '__main__':\
	Pi()

