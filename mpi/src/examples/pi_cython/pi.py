# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:21:24 2013

@author: Sung Bae
"""
import time
import pi_cython as cpi

#@profile
def Pi(num_steps):
	sum = 0
	start = time.time()

	# Call the function implemented in the C extention here
	sum = cpi.loop(num_steps)

	pi = sum/num_steps

	end = time.time()
	print "Pi with %d steps is %.20f in %f secs"\
	 %(num_steps,\
	 pi, end-start)

if __name__ == '__main__':\
	Pi(100000000)

